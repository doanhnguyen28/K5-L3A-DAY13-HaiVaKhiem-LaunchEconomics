"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Mọi con số tính từ cột *_simulated (xem lại, làm lại) được in kèm nhãn [simulated].
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YEU_CAU_THANG = 45_000       # 1.500 yêu cầu/ngày × 30 ngày
PHAM_VI = ['noi_dia', 'hang_nang']
SIM = '[simulated]'


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - max_lan_chay: bỏ các lần chạy có attempt lớn hơn giới hạn; yêu cầu có so_lan_chay lớn hơn
      giới hạn coi là chuyen_nhan_vien, phút xem lại và làm lại bằng 0.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def vnd(x):
    return f'{x:,.0f}'.replace(',', '.')


def pct(x, d=1):
    return f'{x * 100:.{d}f}%'.replace('.', ',')


def nhiem_vu_a(runs, reqs):
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    g = mo_hinh(runs, reqs)
    print(f'Token (mọi lần chạy)             {vnd(g["token"]):>12} đ  đo từ trace')
    print(f'Tool ({runs.tool_calls.sum()} lần gọi)            {vnd(g["tool"]):>12} đ  đo từ trace')
    print(f'Trong đó lần chạy thứ 2 và 3     {vnd(g["chay_lai"]):>12} đ  đo từ trace')
    print(f'Xem lại ({reqs.phut_xem_lai_simulated.sum()} phút)            {vnd(g["xem_lai"]):>12} đ  {SIM}')
    print(f'Làm lại ({reqs.phut_lam_lai_simulated.sum()} phút)           {vnd(g["lam_lai"]):>12} đ  {SIM}')
    print(f'Tổng chi phí                     {vnd(g["tong"]):>12} đ  có phần {SIM}')
    print(f'Số việc thành công               {g["thanh_cong"]:>12}')
    print(f'Chi phí mỗi việc thành công      {vnd(g["cps"]):>12} đ  {SIM}')
    print(f'Hoá đơn token + tool / yêu cầu   {g["hoa_don_moi_yc"]:>12.1f} đ  đo từ trace')
    print(f'→ gấp {g["cps"] / g["hoa_don_moi_yc"]:.1f} lần hoá đơn; làm lại {pct(g["lam_lai"] / g["tong"])}, '
          f'xem lại {pct(g["xem_lai"] / g["tong"])}, giờ nhân viên {pct((g["xem_lai"] + g["lam_lai"]) / g["tong"])} {SIM}')
    khong_tc = len(reqs) - g['thanh_cong']
    he_thong = (g['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'→ Cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay): {vnd(he_thong)} đ = '
          f'{he_thong / BASELINE:.2f}× của 12.000 đ {SIM}')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'{"Loại":10s} {"Số yc":>6s} {"Thành công":>10s} {"Lần chạy/yc":>11s} {"CPS [sim]":>10s} {"So 12.000":>9s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs.loai == loai]
        m = mo_hinh(runs, sub)
        print(f'{loai:10s} {len(sub):>6d} {pct(m["thanh_cong"] / len(sub)):>10s} '
              f'{sub.so_lan_chay.mean():>11.2f} {vnd(m["cps"]):>8s} đ {m["cps"] / BASELINE:>8.2f}×')
    print('Tỉ lệ ok theo lần thử (chạy lại có giúp không):')
    ok = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
          .assign(ok=lambda d: (d.status == 'ok').astype(float))
          .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print(ok.map(lambda v: '' if pd.isna(v) else pct(v)).to_string())

    print('\n=== A4 · Cộng chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    sc = reqs[reqs.loai.isin(PHAM_VI)]
    m = mo_hinh(runs, sc)
    print(f'Phạm vi: tổng {vnd(m["tong"])} đ / {m["thanh_cong"]} việc thành công = {vnd(m["cps"])} đ {SIM}')
    for ten, kl in [('45.000 yc/tháng', YEU_CAU_THANG), ('Một nửa khối lượng', YEU_CAU_THANG / 2)]:
        tc_thang = kl * m['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong = m['cps'] + co_dinh
        print(f'{ten:20s} {vnd(tc_thang):>7s} việc/tháng · cố định {vnd(co_dinh)} đ/việc · '
              f'tổng {vnd(tong)} đ = {tong / BASELINE:.2f}× {SIM}')
    return g


def nhiem_vu_b(runs, reqs, goc):
    print('\n=== B1 · Đổi từng yếu tố ===')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":28s} {vnd(goc["cps"]):>7s} đ {SIM}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {vnd(cps):>7s} đ {(cps / goc["cps"] - 1) * 100:+6.1f}% {SIM}')

    print('\n=== B2 · Đổi một cặp ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Giá token ×2 + xem lại ×2: {vnd(cap)} đ ({(cap / goc["cps"] - 1) * 100:+.1f}%) {SIM}'
          ' = tổng hai tác động riêng (mô hình cộng tuyến tính)')
    print('Xếp hạng: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên')

    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    print(f'{"Giới hạn":8s} {"Tổng trợ lý":>12s} {"Không TC":>8s} {"Cả hệ thống":>12s} {"CPS":>7s}')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        print(f'{k} lần    {vnd(m["tong"]):>12s} {khong_tc:>8d} {vnd(m["tong"] + khong_tc * BASELINE):>12s} '
              f'{vnd(m["cps"]):>7s}  {SIM}')

    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang) ===')
    sc = reqs[reqs.loai.isin(PHAM_VI)]
    runs_sc = runs[runs.request_id.isin(sc.request_id)]
    co_ok = runs_sc.loc[runs_sc.status == 'ok', 'request_id'].nunique()
    so_lam_lai = int((sc.ket_qua == 'lam_lai').sum())
    token_tool = (runs_sc.tokens_in / 1000 * GIA_VAO + runs_sc.tokens_out / 1000 * GIA_RA
                  + runs_sc.tool_calls * GIA_TOOL).sum()
    thanh_cong = int((sc.ket_qua == 'thanh_cong').sum())
    phut_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_lam_lai in (9, phut_tb):
        tong = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_lam_lai * LUONG_PHUT + token_tool
        cps = tong / thanh_cong
        hoa_von = (BASELINE * thanh_cong - so_lam_lai * phut_lam_lai * LUONG_PHUT - token_tool) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {phut_lam_lai:4.1f} phút: ({co_ok} × 5 phút + {so_lam_lai} ca làm lại + token/tool '
              f'{vnd(token_tool)} đ) / {thanh_cong} = {vnd(cps)} đ = {cps / BASELINE:.2f}× · '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút {SIM}')


def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def nhiem_vu_d(reqs, icc=0.02, nhan_vien=40):
    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n = co_mau(0.70, 0.75)
    print(f'a) Chia theo yêu cầu: {n} yêu cầu mỗi nhóm')
    de = 1 + (75 - 1) * icc
    n_b = math.ceil(n * de)
    can_nguoi = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de:.2f}, n = {n_b} mỗi nhóm → {can_nguoi} người mỗi nhóm, '
          f'tổng {2 * can_nguoi} > {nhan_vien}: không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa 20 / {icc} = {20 / icc:.0f} < {n}: không đạt')
    print(f'd) 6 depot mỗi nhóm: tối đa 6 / {icc} = {6 / icc:.0f}')
    n6 = co_mau(0.70, 0.76)
    m = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    print(f'e) Mức chênh 6 điểm ({n6} mỗi nhóm), 20 người mỗi nhóm: m ≥ {m} yêu cầu mỗi người '
          f'(DE {1 + (m - 1) * icc:.2f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        p5 = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05)
        print(f'   Nếu tác động thật chỉ 5 điểm, power với n = {n6} mỗi nhóm: {p5:.2f}')
    except ImportError:
        print('   (cài statsmodels để tính power ở mức 5 điểm)')
    mo_lai = reqs.mo_lai_trong_7_ngay.mean()
    mo_lai_sc = reqs[reqs.loai.isin(PHAM_VI)].mo_lai_trong_7_ngay.mean()
    print(f'Tỉ lệ mở lại 7 ngày hiện tại: {pct(mo_lai, 2)} ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)}); '
          f'trong phạm vi noi_dia + hang_nang: {pct(mo_lai_sc, 2)}')


def nhiem_vu_e(reqs):
    print('\n=== E1 · Tính thử ba chỉ số (cột đo được, không simulated) ===')
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0))
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'Chính: đóng trong 24h và không mở lại 7 ngày = {pct(chinh.mean(), 2)} ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng: bỏ qua gợi ý (sua + bo) / được xem lại = {pct(bo_qua.mean(), 2)} ({bo_qua.sum()}/{len(xem)})')
    print(f'An toàn: mở lại trong 7 ngày = {pct(an_toan.mean(), 2)} ({an_toan.sum()}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    goc = nhiem_vu_a(runs, reqs)
    nhiem_vu_b(runs, reqs, goc)
    nhiem_vu_d(reqs)
    nhiem_vu_e(reqs)
