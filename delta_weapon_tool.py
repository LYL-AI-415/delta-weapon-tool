import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import string
import math

# ==================== 内置热门改枪码库（参考抖音/主播方案） ====================
# 格式："枪械名": [("改装名称", "改枪码", "适用场景")]
HOT_CODES = {
    # ========== 原有枪械（保留） ==========
    "M4A1": [
        ("激光远射流", "M4A1-X8K2PL9W", "中远距离，后坐力极低"),
        ("近战腰射王", "M4A1-C3M7QY1V", "室内腰射精度极高"),
        ("全能平衡", "M4A1-T5R9BN6L", "开镜快，适合跑打"),
        ("稳如磐石", "M4A1-J2H4FG0D", "蹲点架枪，后坐力几乎为零"),
    ],
    "MP5": [
        ("无脑腰射", "MP5-R7U3EP5S", "贴脸腰射无敌"),
        ("跑打鬼畜", "MP5-K4W2MN8X", "移动开镜惩罚极小"),
        ("消音渗透", "MP5-A9Q1BZ3Y", "绕后偷人专用"),
    ],
    "AK-47": [
        ("暴力压枪", "AK47-G6T0VN4I", "近中距离爆发，后坐力可控"),
        ("远程单点", "AK47-L8P2CX7O", "高倍镜单点，伤害爆炸"),
        ("丐版战神", "AK47-Z5R1ME9W", "便宜好用，垂直后坐力优化"),
    ],
    "AWM": [
        ("瞬狙快切", "AWM-U3S7QF2D", "开镜极快，拉栓流畅"),
        ("超远狙击", "AWM-Y6E0HJ1K", "15倍镜，下坠极小"),
        ("消音幽灵", "AWM-V4B8NP3M", "消音+快速拉栓，来无影去无踪"),
    ],
    "M700": [
        ("平民神狙", "M700-D2W5XL6T", "性价比极高，拉栓快"),
        ("连狙压制", "M700-H8K3RC9Q", "半自动改装，中距离火力压制"),
    ],

    # ========== 聪聪方案（已整合） ==========
    "SR3M": [
        ("双修顶配版（射程腰射）", "6K25SBS0EU90O684D8QL5", "远近兼顾，腰射开镜双修"),
        ("双修顶配版（极限射程）", "6K25SL40EU90O684D8QL5", "极限射程对枪"),
        ("性价比撕咬版", "6K26PBC0B1RRH96DI8AIT", "25万低价高性价比"),
        ("高改撕咬版", "6K26OH0049H3TLFDHMKHO", "35万高改装近战撕咬"),
    ],
    "KC17": [
        ("超性价比版", "6KI9THS0EU90O684D8QL5", "30万超高性价比"),
        ("短管高改版", "6KI9U5O0EU90O684D8QL5", "42万短管高机动"),
        ("短管FFC顶配版", "6KI9V3C0EU90O684D8QL5", "55万短管顶配，开镜极快"),
        ("长管密令沙暴顶配版", "6KI9V9C0EU90O684D8QL5", "55万长管稳定远射"),
        ("长管FFC倍镜版", "6KIA01C0EU90O684D8QL5", "60万长管倍镜，远距离压制"),
        ("长管密令沙暴倍镜版", "6KI9VQG0EU90O684D8QL5", "60万长管沙暴倍镜"),
    ],
    "MK47（余烬）": [
        ("共二主宰版（均衡稳定）", "6KIVVQO049H3TLFDHMKHO", "均衡稳定，适合大多数玩家"),
        ("共振影袭版（上手简单）", "6KJ01S4049H3TLFDHMKHO", "后坐力友好，新手神器"),
        ("相位CT版（正据枪）", "6KJ029G049H3TLFDHMKHO", "CT据枪流，开镜快精度高"),
        ("消音版幻影主宰版", "6KJ04P0049H3TLFDHMKHO", "消音隐匿，偷人于无形"),
        ("消音版共一影袭版", "6KJ0520049H3TLFDHMKHO", "消音高机动影袭"),
    ],
    "RM277": [
        ("重型一体超性价比版", "6KO8LD40EU90O684D8QL5", "24万重火力入门"),
        ("重型一体中改加强版（可改倍镜）", "6KO9OIG0B1RRH96DI8AIT", "28万可加装倍镜"),
        ("重型一体高改版（可改倍镜）", "6KO9ODO0B1RRH96DI8AIT", "34万高配重火力"),
    ],
    "AKM（颗秒）": [
        ("纯粹粑粑版", "6KOT7FO0EU90O684D8QL5", "18万超低价，上手即用"),
        ("强化粑粑版", "6KOT84K0EU90O684D8QL5", "纯粹版的加强版本"),
        ("满改A版（沙暴锚点）", "6KOT8T80EU90O684D8QL5", "30万沙暴枪管满改"),
        ("满改B版（俄消UR）", "6KOTQBS0B1RRH96DI8AIT", "30万俄制消音器满改"),
    ],
    "ASH12": [
        ("双发腰射双修版（推荐15精校）", "6KHV6TC049H3TLFDHMKHO", "腰射开镜双修，15精校推荐"),
        ("双发共振开镜版（推荐0/30精校）", "6KHV6VS049H3TLFDHMKHO", "开镜流，0/30精校"),
        ("常规满改（共振二代）", "6K4QSNC0B1RRH96DI8AIT", "共振二代满改"),
        ("常规满改（幻影握把）", "6K4QSR80B1RRH96DI8AIT", "幻影握把满改"),
    ],
    "MK4（全自动）": [
        ("腰射性价比版", "6K3QSVO049H3TLFDHMKHO", "25万腰射入门"),
        ("腰射中改版（QR枪托更稳）", "6K3QSH0049H3TLFDHMKHO", "32万QR枪托，更稳"),
        ("腰射中改版（EC阻手更准）", "6K3QSMO049H3TLFDHMKHO", "33万EC阻手，更准"),
        ("腰射高改版（全游戏最准腰射）", "6K3QT3K049H3TLFDHMKHO", "37万，全游戏最准腰射"),
    ],
    "K437": [
        ("双流骨架究极顶配版", "6K44FU4049H3TLFDHMKHO", "45万，S9季中赛新"),
        ("双流CT究极顶配版", "6K45BC0049H3TLFDHMKHO", "45万，S9季中赛新"),
        ("双垂直究极顶配版", "6K44G5K049H3TLFDHMKHO", "45万，S9季中赛新"),
        ("倍镜高改版", "6K44GP4049H3TLFDHMKHO", "38万，S9季中赛新"),
        ("均衡高改版", "6K44HB0049H3TLFDHMKHO", "35万，S9季中赛新"),
    ],
    "M14": [
        ("新共振三代稳定型改法", "6JR7PJ40B0GKDDOTE9T6Q", "稳定型"),
        ("新共振三代高操控改法", "6JR7QJ80B0GKDDOTE9T6Q", "高操控"),
        ("共振人体CT托版", "6JR7RNG0B0GKDDOTE9T6Q", "CT托"),
        ("共振人体影袭版", "6JR7RUO0B0GKDDOTE9T6Q", "影袭版"),
        ("共振二代标准版", "6JR7SPS0B0GKDDOTE9T6Q", "二代标准"),
        ("共振二代弹鼓版", "6JR7T000B0GKDDOTE9T6Q", "弹鼓版"),
    ],
    "M7": [
        ("双流CT顶配版", "6JQJDAK0BAC7RIM3B0293", "CT顶配"),
        ("消音CT顶配版", "6JQJDMS0BAC7RIM3B0293", "消音CT"),
        ("共振二代顶配版", "6JQJE200BAC7RIM3B0293", "共振二代顶配"),
        ("共振二代锚点版", "6JQKCVO0B0GKDDOTE9T6Q", "共振锚点"),
    ],
    "MK47（鏖战）": [
        ("无后坐BUG改法A（快速开镜）", "6JU5M3G0EU90O684D8QL5", "快速开镜"),
        ("无后坐BUG改法B（极限稳定）", "6JU5OF40EU90O684D8QL5", "极限稳定"),
        ("腰射双修A", "6JU6UUC0EU90O684D8QL5", "腰射双修A"),
        ("腰射双修B", "6JU6V2G0EU90O684D8QL5", "腰射双修B"),
    ],
    "MP7（月影）": [
        ("极限腰射双修顶配", "6JVHO400E0LL9IRHUI52L", "腰射双修"),
        ("极限射程双修顶配", "6JVHOKG0E0LL9IRHUI52L", "射程双修"),
        ("短管极限腰射顶配", "6JVREE40B0GKDDOTE9T6Q", "短管腰射"),
        ("增强枪管双修顶配", "6JVRF600B0GKDDOTE9T6Q", "增强双修"),
    ],
    "腾龙": [
        ("经典UR双水平满改（30发）", "6K1HVGK049H3TLFDHMKHO", "UR双水平，30发"),
        ("S9推荐CT双水平满改（30发）", "6K1HVO4049H3TLFDHMKHO", "CT双水平，30发"),
        ("S9推荐CT双水平满改（45发）", "6K1I0DG049H3TLFDHMKHO", "CT双水平，45发"),
    ],
}

# ==================== 武器数据库（保持不变） ====================
WEAPON_DB = {
    "M4A1": {"type": "突击步枪", "适合": "均衡型，中距离", "后坐力等级": 3, "射速等级": 3, "伤害等级": 2},
    "MP5":  {"type": "冲锋枪",   "适合": "近战高速，高机动", "后坐力等级": 1, "射速等级": 5, "伤害等级": 1},
    "AK-47":{"type": "突击步枪", "适合": "高伤害，后坐力大", "后坐力等级": 5, "射速等级": 2, "伤害等级": 4},
    "AWM":  {"type": "狙击步枪", "适合": "一击致命，极低容错", "后坐力等级": 5, "射速等级": 1, "伤害等级": 5},
    "M700": {"type": "射手步枪", "适合": "灵活狙击，节奏快", "后坐力等级": 4, "射速等级": 2, "伤害等级": 4},
}

# ==================== 主界面（增强版） ====================
class WeaponAdvisorPro:
    def __init__(self, root):
        self.root = root
        self.root.title("三角洲行动 - 枪械私人顾问 Pro")
        self.root.geometry("600x850")
        self.root.resizable(False, False)

        # 用户测试数据
        self.dpi = tk.IntVar(value=800)
        self.reaction_time = tk.DoubleVar(value=250.0)
        self.dpi_measurements = []  # 存储多次测量

        # 枪械习惯
        self.pref_type = tk.StringVar(value="自动选择")
        self.pref_range = tk.StringVar(value="中距离")
        self.pref_style = tk.StringVar(value="均衡")

        self.create_widgets()

    # ---------- UI 构建 ----------
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill="both", expand=True)

        # 标题
        ttk.Label(main_frame, text="三角洲行动 · 枪械私人顾问 Pro", font=("微软雅黑", 16, "bold")).pack(pady=5)

        # 笔记本分页
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill="both", expand=True, pady=5)

        # 第1页：DPI测试
        dpi_tab = ttk.Frame(notebook)
        notebook.add(dpi_tab, text="① DPI 测试 (精准)")
        self.build_dpi_tab(dpi_tab)

        # 第2页：反应测试
        rt_tab = ttk.Frame(notebook)
        notebook.add(rt_tab, text="② 反应速度")
        self.build_rt_tab(rt_tab)

        # 第3页：枪械习惯
        pref_tab = ttk.Frame(notebook)
        notebook.add(pref_tab, text="③ 枪械习惯")
        self.build_pref_tab(pref_tab)

        # 第4页：结果分析
        result_tab = ttk.Frame(notebook)
        notebook.add(result_tab, text="④ 推荐方案")
        self.build_result_tab(result_tab)

        # 底部全局分析按钮
        ttk.Button(main_frame, text="🔍 综合分析并生成最终方案", command=self.full_analyze, padding=10).pack(pady=10)

    def build_dpi_tab(self, tab):
        frame = ttk.Frame(tab, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="📏 精准 DPI 测量（A4纸辅助法）", font=("微软雅黑", 12, "bold")).pack()
        ttk.Label(frame, text="拿一张A4纸，宽度刚好21cm，对着屏幕，\n鼠标从左移到右，重复3次取平均。", font=("微软雅黑", 9)).pack(pady=5)

        self.dpi_canvas = tk.Canvas(frame, height=40, bg="lightgray")
        self.dpi_canvas.pack(fill="x", pady=5)
        self.dpi_canvas.bind("<Button-1>", self.start_dpi_measure)
        self.dpi_canvas.bind("<B1-Motion>", self.update_dpi_measure)
        self.dpi_canvas.bind("<ButtonRelease-1>", self.end_dpi_measure)

        self.dpi_status = ttk.Label(frame, text="按住左键从纸左边划到右边，松开后自动记录", foreground="gray")
        self.dpi_status.pack()
        self.dpi_progress = ttk.Label(frame, text="已完成 0/3 次")
        self.dpi_progress.pack()

        ttk.Label(frame, text="当前平均 DPI：").pack(side="left")
        ttk.Label(frame, textvariable=self.dpi, foreground="red", font=("微软雅黑", 11, "bold")).pack(side="left")
        ttk.Button(frame, text="手动输入", command=self.manual_dpi).pack(side="right", padx=5)
        ttk.Button(frame, text="重置测量", command=self.reset_dpi).pack(side="right")

    def build_rt_tab(self, tab):
        frame = ttk.Frame(tab, padding=10)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="🧠 反应速度测试", font=("微软雅黑", 12, "bold")).pack()
        self.rt_btn = tk.Button(frame, text="开始反应测试（共5次）", bg="gray", font=("微软雅黑", 12),
                                command=self.start_rt_test)
        self.rt_btn.pack(pady=10, ipadx=20)
        ttk.Label(frame, text="平均反应时间(ms)：").pack(side="left")
        ttk.Label(frame, textvariable=self.reaction_time, foreground="red", font=("微软雅黑", 11, "bold")).pack(side="left")

    def build_pref_tab(self, tab):
        frame = ttk.Frame(tab, padding=10)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="⚙️ 枪械使用习惯", font=("微软雅黑", 12, "bold")).pack(pady=5)

        # 偏好枪型
        ttk.Label(frame, text="偏好武器类型：").pack(anchor="w")
        type_combo = ttk.Combobox(frame, textvariable=self.pref_type,
                                  values=["自动选择", "突击步枪", "冲锋枪", "狙击步枪", "射手步枪"])
        type_combo.pack(fill="x", pady=2)

        # 交战距离
        ttk.Label(frame, text="主要交战距离：").pack(anchor="w")
        range_combo = ttk.Combobox(frame, textvariable=self.pref_range,
                                   values=["近距离", "中距离", "远距离", "混合"])
        range_combo.pack(fill="x", pady=2)

        # 射击风格
        ttk.Label(frame, text="射击风格：").pack(anchor="w")
        style_combo = ttk.Combobox(frame, textvariable=self.pref_style,
                                   values=["泼水/扫射", "快速点射", "单点精准", "均衡"])
        style_combo.pack(fill="x", pady=2)

        ttk.Label(frame, text="（系统会结合DPI和反应速度，从热门改枪码中为你匹配）", font=("微软雅黑", 8, "italic")).pack(pady=10)

    def build_result_tab(self, tab):
        frame = ttk.Frame(tab, padding=10)
        frame.pack(fill="both", expand=True)
        self.result_text = tk.Text(frame, height=25, width=65, font=("微软雅黑", 10), wrap="word")
        self.result_text.pack()

    # ---------- DPI 精准测量（A4纸21cm） ----------
    def start_dpi_measure(self, event):
        self.dpi_testing = True
        self.dpi_start_x = event.x
        self.dpi_pixel_moved = 0
        self.dpi_canvas.config(bg="orange")

    def update_dpi_measure(self, event):
        if self.dpi_testing:
            self.dpi_pixel_moved = abs(event.x - self.dpi_start_x)

    def end_dpi_measure(self, event):
        if not self.dpi_testing:
            return
        self.dpi_testing = False
        self.dpi_canvas.config(bg="lightgray")
        # A4纸宽度 = 21 cm，转换为英寸 ≈ 8.2677 英寸
        physical_inch = 8.2677
        if self.dpi_pixel_moved < 50:
            messagebox.showwarning("无效测量", "移动距离太短，请确保从纸的一边划到另一边（21cm）")
            return
        calc_dpi = int(self.dpi_pixel_moved / physical_inch)
        calc_dpi = max(100, min(12000, calc_dpi))
        self.dpi_measurements.append(calc_dpi)
        n = len(self.dpi_measurements)
        self.dpi_progress.config(text=f"已完成 {n}/3 次")
        self.dpi_status.config(text=f"第{n}次测量：{calc_dpi} DPI")

        if n >= 3:
            avg = sum(self.dpi_measurements) / n
            self.dpi.set(round(avg))
            self.dpi_status.config(text=f"平均 DPI：{round(avg)} (基于{n}次测量)")
            self.dpi_measurements.clear()
            self.dpi_progress.config(text="测量完成！可重新测试或手动修正")
        else:
            self.dpi_status.config(text=f"还剩 {3-n} 次测量，继续从左到右滑动鼠标")

    def manual_dpi(self):
        win = tk.Toplevel(self.root)
        win.title("手动输入 DPI")
        ttk.Label(win, text="请输入鼠标 DPI（100-12000）").pack(padx=20, pady=10)
        entry = ttk.Entry(win)
        entry.pack(padx=20)
        def set_dpi():
            try:
                val = int(entry.get())
                if 100 <= val <= 12000:
                    self.dpi.set(val)
                    self.dpi_measurements.clear()
                    self.dpi_progress.config(text="已手动设定")
                    win.destroy()
                else:
                    messagebox.showwarning("错误", "范围 100-12000")
            except:
                messagebox.showwarning("错误", "请输入整数")
        ttk.Button(win, text="确定", command=set_dpi).pack(pady=10)

    def reset_dpi(self):
        self.dpi_measurements.clear()
        self.dpi_progress.config(text="已重置，重新测3次")
        self.dpi_status.config(text="按住左键从纸左边划到右边")

    # ---------- 反应测试 ----------
    def start_rt_test(self):
        self.rt_btn.config(state="disabled", text="等待绿色...", bg="gray")
        self.root.update()
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_green)

    def show_green(self):
        self.rt_btn.config(bg="green", text="点击！！！", state="normal")
        self.rt_start = time.time()
        self.rt_btn.config(command=self.record_rt)

    def record_rt(self):
        rt = (time.time() - self.rt_start) * 1000
        if not hasattr(self, 'rt_list'):
            self.rt_list = []
        self.rt_list.append(rt)
        self.rt_btn.config(bg="gray", text="继续测试", command=self.start_rt_test)
        if len(self.rt_list) >= 5:
            avg = sum(self.rt_list) / len(self.rt_list)
            self.reaction_time.set(round(avg, 1))
            self.rt_btn.config(bg="lightgray", text="测试完成", state="disabled", command=None)
            messagebox.showinfo("反应测试", f"5次平均：{avg:.1f} ms")
            self.rt_list = []

    # ---------- 综合分析与推荐 ----------
    def full_analyze(self):
        dpi_val = self.dpi.get()
        rt_val = self.reaction_time.get()

        # 用户画像
        if dpi_val >= 800:
            dpi_cat = "高DPI"
        else:
            dpi_cat = "低DPI"
        if rt_val <= 200:
            rt_cat = "快反应"
        else:
            rt_cat = "慢反应"

        # 读取习惯
        pref_type = self.pref_type.get()
        pref_range = self.pref_range.get()
        pref_style = self.pref_style.get()

        # 智能推荐枪械
        weapon_key = self.recommend_weapon(dpi_val, rt_val, pref_type, pref_range, pref_style)

        # 从热门码中匹配最适合的
        matched_code = self.match_hot_code(weapon_key, pref_range, pref_style)

        result = f"""
【用户数据】
DPI：{dpi_val} ({dpi_cat})   |   反应时间：{rt_val} ms ({rt_cat})
偏好武器：{pref_type}   |   交战距离：{pref_range}   |   射击风格：{pref_style}

【最终推荐】
推荐枪械：{weapon_key} ({WEAPON_DB[weapon_key]['type']})
特点：{WEAPON_DB[weapon_key]['适合']}

【热门改枪码】
改装名称：{matched_code[0]}
改枪码：   {matched_code[1]}
适用场景：{matched_code[2]}

（该码来自抖音/主播实测方案，可在游戏内导入）
        """
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def recommend_weapon(self, dpi, rt, pref_type, pref_range, pref_style):
        # 如果用户指定了类型，就在该类型内选；否则综合选
        candidates = list(WEAPON_DB.keys())
        if pref_type != "自动选择":
            type_map = {
                "突击步枪": ["M4A1", "AK-47"],
                "冲锋枪": ["MP5"],
                "狙击步枪": ["AWM"],
                "射手步枪": ["M700"],
            }
            candidates = type_map.get(pref_type, candidates)

        # 根据DPI和反应微调
        best = None
        best_score = -1
        for w in candidates:
            stats = WEAPON_DB[w]
            score = 0
            # DPI高适合射速快、机动高；低适合稳枪
            if dpi >= 800:
                score += stats["射速等级"] * 2
            else:
                score += (6 - stats["后坐力等级"]) * 2

            # 反应快适合近战；慢适合狙击
            if rt <= 200:
                if stats["type"] in ["冲锋枪", "突击步枪"]:
                    score += 5
            else:
                if stats["type"] in ["狙击步枪", "射手步枪"]:
                    score += 5

            # 距离匹配
            if pref_range == "近距离" and stats["type"] == "冲锋枪":
                score += 10
            elif pref_range == "远距离" and stats["type"] in ["狙击步枪", "射手步枪"]:
                score += 10
            elif pref_range == "中距离" and stats["type"] == "突击步枪":
                score += 8

            if score > best_score:
                best_score = score
                best = w
        return best if best else "M4A1"

    def match_hot_code(self, weapon, distance, style):
        codes = HOT_CODES.get(weapon, HOT_CODES["M4A1"])
        # 简单匹配：近距离 → 腰射/跑打关键词，远距离 → 远射/单点关键词
        best_match = codes[0]
        for name, code, desc in codes:
            if distance == "近距离" and ("腰射" in name or "跑打" in name or "贴脸" in name):
                return (name, code, desc)
            if distance == "远距离" and ("远射" in name or "狙击" in name or "单点" in name):
                return (name, code, desc)
        return best_match

# ==================== 启动 ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponAdvisorPro(root)
    root.mainloop()
