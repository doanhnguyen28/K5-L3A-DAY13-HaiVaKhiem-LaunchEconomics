"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
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


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


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
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn, yêu cầu vượt coi là chuyen_nhan_vien
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy, kể cả lần lỗi. Giá tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3, A4 ----------
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
KHOI_LUONG_THANG = 45_000      # yêu cầu / tháng


def tach_theo_loai(runs, reqs):
    """A3: chi phí mỗi việc thành công theo từng loai."""
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        dong.append(dict(loai=loai, so_yc=len(r), ti_le_tc=kq['thanh_cong'] / len(r),
                         lan_chay_moi_yc=r['so_lan_chay'].mean(), cps=kq['cps'],
                         so_voi_baseline=kq['cps'] / BASELINE))
    return pd.DataFrame(dong)


def ti_le_ok_theo_lan_thu(runs, reqs):
    """A3: tỉ lệ status == ok theo loai × attempt (chạy lại có giúp không)."""
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    return m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


def chi_phi_co_dinh(runs, reqs, ti_le_khoi_luong=1.0):
    """A4: cộng chi phí cố định cho phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pham_vi)
    tc_thang = KHOI_LUONG_THANG * ti_le_khoi_luong * kq['thanh_cong'] / len(reqs)
    co_dinh = CHI_PHI_CO_DINH / tc_thang
    return dict(tc_thang=tc_thang, co_dinh_moi_viec=co_dinh, cps=kq['cps'],
                cps_co_dinh=kq['cps'] + co_dinh, so_voi_baseline=(kq['cps'] + co_dinh) / BASELINE)


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
# TODO CP2 (đã làm)
KICH_BAN = {
    'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':            dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':       dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':            dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':       dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':             dict(luong_phut=2500),
    'Tối đa 2 lần chạy':          dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':             dict(max_lan_chay=1),
}


def bang_do_nhay(runs, reqs):
    """B1 + B2: chi phí mỗi việc thành công khi đổi từng yếu tố và một cặp."""
    goc = mo_hinh(runs, reqs)['cps']
    dong = [dict(kich_ban='Gốc (A2)', cps=goc, thay_doi=0.0)]
    for ten, kw in {**KICH_BAN, 'Cặp: token ×2 + xem lại ×2':
                    dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2)}.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi=(cps / goc - 1) * 100))
    return pd.DataFrame(dong)


def chi_phi_ca_he_thong(runs, reqs):
    """B3: chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay)."""
    dong = []
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        dong.append(dict(gioi_han=k, tong_tro_ly=kq['tong'], khong_thanh_cong=khong_tc,
                         ca_he_thong=kq['tong'] + BASELINE * khong_tc, cps=kq['cps']))
    return pd.DataFrame(dong)


def xem_lai_toan_bo(runs, reqs, phut_xem=5, phut_lam_lai=9):
    """B4: xem lại 100% trong phạm vi noi_dia + hang_nang."""
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    so_co_ok = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA
                  + r['tool_calls'] * GIA_TOOL).sum()
    xem = so_co_ok * phut_xem * LUONG_PHUT
    lam = so_lam_lai * phut_lam_lai * LUONG_PHUT
    tong = token_tool + xem + lam
    tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    hoa_von = (BASELINE * tc - token_tool - lam) / (so_co_ok * LUONG_PHUT)  # phút xem lại tối đa
    return dict(so_yc=len(pv), so_co_ok=so_co_ok, so_lam_lai=so_lam_lai, token_tool=token_tool,
                xem_lai=xem, lam_lai=lam, tong=tong, thanh_cong=tc, cps=tong / tc,
                so_voi_baseline=tong / tc / BASELINE, phut_xem_hoa_von=hoa_von)


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
ICC = 0.02


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (z chính xác)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m − 1) × ICC, m = số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def cau_d1(p1=0.70, icc=ICC):
    """Năm câu D1 và power ở mức 5 điểm khi thiết kế cho mức 6 điểm."""
    n_a = co_mau(p1, p1 + 0.05)
    de_b = he_so_thiet_ke(75, icc)
    n_b = math.ceil(n_a * de_b)
    n_e = co_mau(p1, p1 + 0.06)
    # e: 20m / (1 + (m − 1)·ICC) ≥ n_e  →  m ≥ n_e(1 − ICC) / (20 − n_e·ICC)
    m_e = math.ceil(n_e * (1 - icc) / (20 - n_e * icc))
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        power_5 = NormalIndPower().power(proportion_effectsize(p1 + 0.05, p1), nobs1=n_e, alpha=0.05)
    except ImportError:
        power_5 = None
    return dict(a=n_a, b_de=de_b, b_n=n_b, b_nguoi=math.ceil(n_b / 75),
                c=20 / icc, d=6 / icc, e_n=n_e, e_m=m_e, e_de=he_so_thiet_ke(m_e, icc),
                power_5_diem=power_5)


# ---------- Nhiệm vụ E · Chỉ số ----------
def chi_so_e(reqs):
    """Chỉ số chính, chỉ số dùng, chỉ số an toàn: trả về (tỉ lệ, tử số, mẫu số)."""
    dong = reqs['dong_trong_24h'].astype(int)
    mo_lai = reqs['mo_lai_trong_7_ngay'].astype(int)
    chinh = int(((dong == 1) & (mo_lai == 0)).sum())
    xem = reqs[reqs['duoc_xem_lai'].astype(int) == 1]
    bo_qua = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    an_toan = int((mo_lai == 1).sum())
    return {'Chính': (chinh / len(reqs), chinh, len(reqs)),
            'Dùng': (bo_qua / len(xem), bo_qua, len(xem)),
            'An toàn': (an_toan / len(reqs), an_toan, len(reqs))}


if __name__ == '__main__':
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')   # console Windows mặc định cp1252, không in được tiếng Việt
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"{'gap_hoa_don':12s} {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14.1f} lần")
    nv = ket_qua['xem_lai'] + ket_qua['lam_lai']
    print(f"Tỉ trọng: làm lại {ket_qua['lam_lai'] / ket_qua['tong']:.1%} · xem lại "
          f"{ket_qua['xem_lai'] / ket_qua['tong']:.1%} · giờ nhân viên {nv / ket_qua['tong']:.1%} [simulated]")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu: {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    print('\n== A3 · Theo loại [cps simulated] ==')
    print(tach_theo_loai(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.3f}'))
    print('\nTỉ lệ ok theo lần thử:')
    print(ti_le_ok_theo_lan_thu(runs, reqs).round(3).to_string())

    print('\n== A4 · Chi phí cố định (noi_dia + hang_nang) [simulated] ==')
    for ten, tl in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        a4 = chi_phi_co_dinh(runs, reqs, tl)
        print(f"{ten:20s} TC/tháng {a4['tc_thang']:>8,.0f} · cố định {a4['co_dinh_moi_viec']:>6,.0f} đ"
              f" · tổng {a4['cps_co_dinh']:>6,.0f} đ = {a4['so_voi_baseline']:.2f}×")

    print('\n== B1, B2 · Độ nhạy [simulated] ==')
    for _, d in bang_do_nhay(runs, reqs).iterrows():
        print(f"{d['kich_ban']:28s} {d['cps']:8,.0f} {d['thay_doi']:+6.1f}%")

    print('\n== B3 · Chi phí cả hệ thống theo giới hạn chạy [simulated] ==')
    print(chi_phi_ca_he_thong(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.0f}'))

    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) [simulated] ==')
    pll = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    for phut in [9, round(pll.mean(), 1)]:
        b4 = xem_lai_toan_bo(runs, reqs, phut_lam_lai=phut)
        print(f"Làm lại {phut} phút/ca: tổng {b4['tong']:,.0f} đ / {b4['thanh_cong']} = {b4['cps']:,.0f} đ"
              f" = {b4['so_voi_baseline']:.2f}× · hoà vốn xem lại ≤ {b4['phut_xem_hoa_von']:.1f} phút")
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu (đã làm)
    print('\n== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ==')
    d1 = cau_d1()
    print(f"a) Chia theo yêu cầu: {d1['a']:,} yêu cầu mỗi nhóm")
    print(f"b) Theo nhân viên, m = 75: DE = {d1['b_de']:.2f} → {d1['b_n']:,} mỗi nhóm"
          f" → {d1['b_nguoi']} người mỗi nhóm, tổng {2 * d1['b_nguoi']} > 40: không đủ người")
    print(f"c) 20 nhân viên mỗi nhóm: tối đa {d1['c']:,.0f} < {d1['a']:,}: không đạt")
    print(f"d) 6 depot mỗi nhóm: tối đa {d1['d']:,.0f}")
    print(f"e) Mức chênh 6 điểm ({d1['e_n']} mỗi nhóm), 20 người mỗi nhóm: m ≥ {d1['e_m']}"
          f" yêu cầu mỗi người (DE {d1['e_de']:.2f})")
    if d1['power_5_diem'] is not None:
        print(f"Power ở mức 5 điểm khi n = {d1['e_n']}: {d1['power_5_diem']:.2f}")
    mo_lai = reqs['mo_lai_trong_7_ngay'].astype(int)
    pv = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    print(f"Tỉ lệ mo_lai_trong_7_ngay hiện tại: {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)})"
          f" · trong phạm vi noi_dia + hang_nang: {mo_lai[pv].mean():.2%}")

    print('\n== E · Ba chỉ số trên 1.200 yêu cầu chạy thử ==')
    for ten, (gia_tri, tu, mau) in chi_so_e(reqs).items():
        print(f'{ten:8s} {gia_tri:.2%} ({tu}/{mau})')