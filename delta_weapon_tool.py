import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# ==================== 完整枪械数据库 ====================
WEAPON_DB = {
    "M4A1": {"type": "突击步枪", "适合": "均衡型，中距离", "后坐力等级": 3, "射速等级": 3, "伤害等级": 2},
    "MP5":  {"type": "冲锋枪",   "适合": "近战高速，高机动", "后坐力等级": 1, "射速等级": 5, "伤害等级": 1},
    "AK-47":{"type": "突击步枪", "适合": "高伤害，后坐力大", "后坐力等级": 5, "射速等级": 2, "伤害等级": 4},
    "AWM":  {"type": "狙击步枪", "适合": "一击致命，极低容错", "后坐力等级": 5, "射速等级": 1, "伤害等级": 5},
    "M700": {"type": "射手步枪", "适合": "灵活狙击，节奏快", "后坐力等级": 4, "射速等级": 2, "伤害等级": 4},
    "SR3M": {"type": "冲锋枪",   "适合": "撕咬近战，双修", "后坐力等级": 2, "射速等级": 4, "伤害等级": 2},
    "KC17": {"type": "射手步枪", "适合": "远距离压制，长短管可选", "后坐力等级": 3, "射速等级": 2, "伤害等级": 4},
    "MK47（余烬）": {"type": "突击步枪", "适合": "均衡稳定，影袭/主宰", "后坐力等级": 3, "射速等级": 3, "伤害等级": 3},
    "RM277": {"type": "狙击步枪", "适合": "重型一体，高伤害", "后坐力等级": 4, "射速等级": 1, "伤害等级": 5},
    "AKM（颗秒）": {"type": "突击步枪", "适合": "暴力压枪，低价高伤", "后坐力等级": 5, "射速等级": 2, "伤害等级": 4},
    "ASH12": {"type": "射手步枪", "适合": "双发腰射，近远双修", "后坐力等级": 3, "射速等级": 2, "伤害等级": 4},
    "MK4（全自动）": {"type": "冲锋枪", "适合": "全自动腰射，高机动", "后坐力等级": 2, "射速等级": 5, "伤害等级": 1},
    "K437": {"type": "突击步枪", "适合": "双流骨架/CT顶配，S9新秀", "后坐力等级": 3, "射速等级": 3, "伤害等级": 3},
    "M14": {"type": "射手步枪", "适合": "共振系列，稳定或高操控", "后坐力等级": 3, "射速等级": 2, "伤害等级": 4},
    "M7":  {"type": "射手步枪", "适合": "双流/消音CT顶配", "后坐力等级": 3, "射速等级": 2, "伤害等级": 4},
    "MP7（月影）": {"type": "冲锋枪", "适合": "极限腰射/射程双修", "后坐力等级": 2, "射速等级": 5, "伤害等级": 2},
    "腾龙": {"type": "突击步枪", "适合": "UR/CT双水平满改", "后坐力等级": 3, "射速等级": 3, "伤害等级": 3},
}

# ==================== 热门改枪码（聪聪全系列） ====================
HOT_CODES = {
    "M4A1": [("激光远射流", "M4A1-X8K2PL9W", "中远距离，后坐力极低"),
             ("近战腰射王", "M4A1-C3M7QY1V", "室内腰射精度极高"),
             ("全能平衡", "M4A1-T5R9BN6L", "开镜快，适合跑打"),
             ("稳如磐石", "M4A1-J2H4FG0D", "蹲点架枪")],
    "MP5": [("无脑腰射", "MP5-R7U3EP5S", "贴脸腰射无敌"),
            ("跑打鬼畜", "MP5-K4W2MN8X", "移动开镜惩罚极小"),
            ("消音渗透", "MP5-A9Q1BZ3Y", "绕后偷人")],
    "AK-47": [("暴力压枪", "AK47-G6T0VN4I", "近中距离爆发"),
              ("远程单点", "AK47-L8P2CX7O", "高倍镜单点"),
              ("丐版战神", "AK47-Z5R1ME9W", "便宜好用")],
    "AWM": [("瞬狙快切", "AWM-U3S7QF2D", "开镜极快"),
            ("超远狙击", "AWM-Y6E0HJ1K", "15倍镜"),
            ("消音幽灵", "AWM-V4B8NP3M", "消音拉栓")],
    "M700": [("平民神狙", "M700-D2W5XL6T", "性价比极高"),
             ("连狙压制", "M700-H8K3RC9Q", "半自动火力")],
    "SR3M": [("双修顶配版（射程腰射）", "6K25SBS0EU90O684D8QL5", "远近兼顾"),
             ("双修顶配版（极限射程）", "6K25SL40EU90O684D8QL5", "极限射程"),
             ("性价比撕咬版", "6K26PBC0B1RRH96DI8AIT", "25万"),
             ("高改撕咬版", "6K26OH0049H3TLFDHMKHO", "35万")],
    "KC17": [("超性价比版", "6KI9THS0EU90O684D8QL5", "30万"),
             ("短管高改版", "6KI9U5O0EU90O684D8QL5", "42万"),
             ("短管FFC顶配版", "6KI9V3C0EU90O684D8QL5", "55万"),
             ("长管密令沙暴顶配版", "6KI9V9C0EU90O684D8QL5", "55万"),
             ("长管FFC倍镜版", "6KIA01C0EU90O684D8QL5", "60万"),
             ("长管密令沙暴倍镜版", "6KI9VQG0EU90O684D8QL5", "60万")],
    "MK47（余烬）": [("共二主宰版（均衡稳定）", "6KIVVQO049H3TLFDHMKHO", "均衡"),
                  ("共振影袭版（上手简单）", "6KJ01S4049H3TLFDHMKHO", "新手"),
                  ("相位CT版（正据枪）", "6KJ029G049H3TLFDHMKHO", "CT据枪"),
                  ("消音版幻影主宰版", "6KJ04P0049H3TLFDHMKHO", "消音"),
                  ("消音版共一影袭版", "6KJ0520049H3TLFDHMKHO", "消音影袭")],
    "RM277": [("重型一体超性价比版", "6KO8LD40EU90O684D8QL5", "24万"),
              ("重型一体中改加强版", "6KO9OIG0B1RRH96DI8AIT", "28万可改倍镜"),
              ("重型一体高改版", "6KO9ODO0B1RRH96DI8AIT", "34万可改倍镜")],
    "AKM（颗秒）": [("纯粹粑粑版", "6KOT7FO0EU90O684D8QL5", "18万"),
                  ("强化粑粑版", "6KOT84K0EU90O684D8QL5", "加强"),
                  ("满改A版（沙暴锚点）", "6KOT8T80EU90O684D8QL5", "30万"),
                  ("满改B版（俄消UR）", "6KOTQBS0B1RRH96DI8AIT", "30万")],
    "ASH12": [("双发腰射双修版（15精校）", "6KHV6TC049H3TLFDHMKHO", "腰射双修"),
              ("双发共振开镜版（0/30精校）", "6KHV6VS049H3TLFDHMKHO", "开镜流"),
              ("常规满改（共振二代）", "6K4QSNC0B1RRH96DI8AIT", "共振"),
              ("常规满改（幻影握把）", "6K4QSR80B1RRH96DI8AIT", "幻影")],
    "MK4（全自动）": [("腰射性价比版", "6K3QSVO049H3TLFDHMKHO", "25万"),
                   ("腰射中改版（QR枪托）", "6K3QSH0049H3TLFDHMKHO", "32万"),
                   ("腰射中改版（EC阻手）", "6K3QSMO049H3TLFDHMKHO", "33万"),
                   ("腰射高改版（最准腰射）", "6K3QT3K049H3TLFDHMKHO", "37万")],
    "K437": [("双流骨架究极顶配版", "6K44FU4049H3TLFDHMKHO", "45万"),
             ("双流CT究极顶配版", "6K45BC0049H3TLFDHMKHO", "45万"),
             ("双垂直究极顶配版", "6K44G5K049H3TLFDHMKHO", "45万"),
             ("倍镜高改版", "6K44GP4049H3TLFDHMKHO", "38万"),
             ("均衡高改版", "6K44HB0049H3TLFDHMKHO", "35万")],
    "M14": [("新共振三代稳定型", "6JR7PJ40B0GKDDOTE9T6Q", "稳定"),
            ("新共振三代高操控", "6JR7QJ80B0GKDDOTE9T6Q", "高操控"),
            ("共振人体CT托版", "6JR7RNG0B0GKDDOTE9T6Q", "CT托"),
            ("共振人体影袭版", "6JR7RUO0B0GKDDOTE9T6Q", "影袭"),
            ("共振二代标准版", "6JR7SPS0B0GKDDOTE9T6Q", "标准"),
            ("共振二代弹鼓版", "6JR7T000B0GKDDOTE9T6Q", "弹鼓")],
    "M7": [("双流CT顶配版", "6JQJDAK0BAC7RIM3B0293", "CT顶配"),
           ("消音CT顶配版", "6JQJDMS0BAC7RIM3B0293", "消音CT"),
           ("共振二代顶配版", "6JQJE200BAC7RIM3B0293", "共振二代"),
           ("共振二代锚点版", "6JQKCVO0B0GKDDOTE9T6Q", "锚点")],
    "MP7（月影）": [("极限腰射双修顶配", "6JVHO400E0LL9IRHUI52L", "腰射双修"),
                 ("极限射程双修顶配", "6JVHOKG0E0LL9IRHUI52L", "射程双修"),
                 ("短管极限腰射顶配", "6JVREE40B0GKDDOTE9T6Q", "短管腰射"),
                 ("增强枪管双修顶配", "6JVRF600B0GKDDOTE9T6Q", "增强双修")],
    "腾龙": [("经典UR双水平满改（30发）", "6K1HVGK049H3TLFDHMKHO", "30发"),
             ("S9推荐CT双水平满改（30发）", "6K1HVO4049H3TLFDHMKHO", "30发"),
             ("S9推荐CT双水平满改（45发）", "6K1I0DG049H3TLFDHMKHO", "45发")],
    "MK47（鏖战）": [("无后坐BUG改法A（快速开镜）", "6JU5M3G0EU90O684D8QL5", "快速开镜"),
                  ("无后坐BUG改法B（极限稳定）", "6JU5OF40EU90O684D8QL5", "极限稳定"),
                  ("腰射双修A", "6JU6UUC0EU90O684D8QL5", "腰射双修A"),
                  ("腰射双修B", "6JU6V2G0EU90O684D8QL5", "腰射双修B")],
}

# ==================== UI 美化设置 ====================
BG_COLOR = "#F0F3F7"
ACCENT_COLOR = "#2C3E50"
BTN_COLOR = "#2980B9"
BTN_HOVER = "#3498DB"

class WeaponAdvisorPro:
    def __init__(self, root):
        self.root = root
        self.root.title("三角洲行动 · 枪械私人顾问 Pro")
        self.root.geometry("720x880")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # 主题与样式
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background=BG_COLOR, font=("微软雅黑", 10))
        style.configure("TLabelframe", background=BG_COLOR, font=("微软雅黑", 10, "bold"))
        style.configure("TLabelframe.Label", background=BG_COLOR)
        style.configure("TButton", font=("微软雅黑", 10), padding=6)
        style.configure("TCombobox", font=("微软雅黑", 10))
        style.configure("Accent.TButton", background=BTN_COLOR, foreground="white")
        style.map("Accent.TButton", background=[("active", BTN_HOVER)])

        # 变量
        self.dpi = tk.IntVar(value=800)
        self.reaction_time = tk.DoubleVar(value=250.0)
        self.dpi_measurements = []

        self.pref_type = tk.StringVar(value="自动选择")
        self.pref_range = tk.StringVar(value="中距离")
        self.pref_style = tk.StringVar(value="均衡")
        # 新增变量
        self.pref_recoil = tk.StringVar(value="垂直优先")
        self.pref_suppressor = tk.BooleanVar(value=False)
        self.pref_hipfire_grip = tk.BooleanVar(value=False)
        self.pref_scope = tk.StringVar(value="红点/全息")
        self.pad_size = tk.StringVar(value="中号（30-40cm）")
        self.screen_res = tk.StringVar(value="1920x1080")
        self.in_game_sens = tk.DoubleVar(value=1.0)

        self.selected_weapon = tk.StringVar(value="M4A1")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # 标题
        title = ttk.Label(main_frame, text="三角洲行动 · 枪械私人顾问 Pro",
                          font=("微软雅黑", 18, "bold"), foreground=ACCENT_COLOR, background=BG_COLOR)
        title.pack(pady=(0,10))

        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill="both", expand=True)

        # 选项卡
        notebook.add(self.build_dpi_tab(), text="① DPI 测试 (精准)")
        notebook.add(self.build_rt_tab(), text="② 反应速度")
        notebook.add(self.build_pref_tab(), text="③ 高级战斗偏好")
        notebook.add(self.build_result_tab(), text="④ 推荐方案 & 查询")

        # 底部按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="🔍 综合分析并生成推荐", style="Accent.TButton",
                   command=self.full_analyze).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="📋 直接查询选中枪械", style="Accent.TButton",
                   command=self.query_selected).pack(side="left", padx=10)

    # ---------- DPI 测试（美化版） ----------
    def build_dpi_tab(self):
        tab = ttk.Frame()
        tab.configure(padding=15)

        ttk.Label(tab, text="📏 精准 DPI 测量（A4纸辅助法）", font=("微软雅黑", 14, "bold")).pack()
        ttk.Label(tab, text="拿一张A4纸（宽度21cm），鼠标从左移到右，重复3次取平均。",
                  font=("微软雅黑", 9), foreground="gray").pack(pady=5)

        self.dpi_canvas = tk.Canvas(tab, height=50, bg="#D5D8DC", highlightthickness=0)
        self.dpi_canvas.pack(fill="x", pady=10)
        self.dpi_canvas.bind("<Button-1>", self.start_dpi)
        self.dpi_canvas.bind("<B1-Motion>", self.update_dpi)
        self.dpi_canvas.bind("<ButtonRelease-1>", self.end_dpi)

        self.dpi_status = ttk.Label(tab, text="按住左键从纸左边划到右边，松开后自动记录", foreground="gray")
        self.dpi_status.pack()
        self.dpi_progress = ttk.Label(tab, text="已完成 0/3 次", font=("微软雅黑", 10, "bold"))
        self.dpi_progress.pack(pady=5)

        val_frame = ttk.Frame(tab)
        val_frame.pack(fill="x", pady=5)
        ttk.Label(val_frame, text="当前平均 DPI：", font=("微软雅黑", 11)).pack(side="left")
        ttk.Label(val_frame, textvariable=self.dpi, foreground="#E74C3C", font=("微软雅黑", 14, "bold")).pack(side="left")
        ttk.Button(val_frame, text="手动输入", command=self.manual_dpi).pack(side="right", padx=5)
        ttk.Button(val_frame, text="重置测量", command=self.reset_dpi).pack(side="right")
        return tab

    # ---------- 反应测试 ----------
    def build_rt_tab(self):
        tab = ttk.Frame(padding=15)
        ttk.Label(tab, text="🧠 反应速度测试", font=("微软雅黑", 14, "bold")).pack(pady=10)
        self.rt_btn = tk.Button(tab, text="开始反应测试（共5次）", bg="#7F8C8D", fg="white",
                                font=("微软雅黑", 14, "bold"), relief="flat", padx=30, pady=10,
                                command=self.start_rt)
        self.rt_btn.pack(pady=20)
        ttk.Label(tab, text="平均反应时间(ms)：", font=("微软雅黑", 11)).pack(side="left")
        ttk.Label(tab, textvariable=self.reaction_time, foreground="#E74C3C", font=("微软雅黑", 14, "bold")).pack(side="left")
        return tab

    # ---------- 高级战斗偏好（大幅扩展） ----------
    def build_pref_tab(self):
        tab = ttk.Frame(padding=15)
        ttk.Label(tab, text="⚙️ 高级战斗偏好", font=("微软雅黑", 14, "bold")).pack(pady=(0,10))

        # 使用多个 LabelFrame 分组
        group1 = ttk.LabelFrame(tab, text="基本武器偏好", padding=10)
        group1.pack(fill="x", pady=5)
        ttk.Label(group1, text="偏好武器类型：").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group1, textvariable=self.pref_type,
                     values=["自动选择", "突击步枪", "冲锋枪", "狙击步枪", "射手步枪"],
                     state="readonly", width=18).grid(row=0, column=1, padx=5)

        ttk.Label(group1, text="主要交战距离：").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group1, textvariable=self.pref_range,
                     values=["近距离", "中距离", "远距离", "混合"],
                     state="readonly", width=18).grid(row=1, column=1, padx=5)

        ttk.Label(group1, text="射击风格：").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group1, textvariable=self.pref_style,
                     values=["泼水/扫射", "快速点射", "单点精准", "均衡"],
                     state="readonly", width=18).grid(row=2, column=1, padx=5)

        # 第二组：配件与操作
        group2 = ttk.LabelFrame(tab, text="操作与配件倾向", padding=10)
        group2.pack(fill="x", pady=5)
        ttk.Label(group2, text="压枪习惯：").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group2, textvariable=self.pref_recoil,
                     values=["垂直优先", "水平优先", "无脑压枪", "微控点射"],
                     state="readonly", width=18).grid(row=0, column=1, padx=5)

        ttk.Label(group2, text="瞄具偏好：").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group2, textvariable=self.pref_scope,
                     values=["红点/全息", "2-4倍镜", "高倍镜(6倍以上)", "机瞄/无"],
                     state="readonly", width=18).grid(row=1, column=1, padx=5)

        ttk.Checkbutton(group2, text="偏爱消音器", variable=self.pref_suppressor).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Checkbutton(group2, text="偏爱腰射握把", variable=self.pref_hipfire_grip).grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # 第三组：外设环境
        group3 = ttk.LabelFrame(tab, text="外设与环境（辅助推荐）", padding=10)
        group3.pack(fill="x", pady=5)
        ttk.Label(group3, text="鼠标垫尺寸：").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group3, textvariable=self.pad_size,
                     values=["小号(<30cm)", "中号（30-40cm）", "大号（40-50cm）", "桌垫级(>50cm)"],
                     state="readonly", width=18).grid(row=0, column=1, padx=5)

        ttk.Label(group3, text="屏幕分辨率：").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(group3, textvariable=self.screen_res,
                     values=["1920x1080", "2560x1440", "3840x2160", "1366x768"],
                     state="readonly", width=18).grid(row=1, column=1, padx=5)

        ttk.Label(group3, text="游戏内鼠标灵敏度：").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        sens_frame = ttk.Frame(group3)
        sens_frame.grid(row=2, column=1, padx=5)
        ttk.Entry(sens_frame, textvariable=self.in_game_sens, width=10).pack(side="left")
        ttk.Label(sens_frame, text="（例：1.0）").pack(side="left")

        return tab

    # ---------- 结果与查询页 ----------
    def build_result_tab(self):
        tab = ttk.Frame(padding=15)
        query_frame = ttk.LabelFrame(tab, text="📌 直接查询任意枪械的改枪码", padding=10)
        query_frame.pack(fill="x", pady=5)
        ttk.Label(query_frame, text="选择枪械：").pack(side="left")
        weapon_list = list(HOT_CODES.keys())
        self.weapon_combo = ttk.Combobox(query_frame, textvariable=self.selected_weapon,
                                         values=weapon_list, state="readonly", width=22)
        self.weapon_combo.pack(side="left", padx=10)
        ttk.Button(query_frame, text="查询", style="Accent.TButton", command=self.query_selected).pack(side="left")

        self.result_text = tk.Text(tab, height=24, width=75, font=("微软雅黑", 10), wrap="word",
                                   bg="white", relief="solid", bd=1)
        self.result_text.pack(pady=10, fill="both", expand=True)
        return tab

    # ---------- DPI 测量逻辑（不变） ----------
    def start_dpi(self, event):
        self.dpi_testing = True
        self.dpi_start_x = event.x
        self.dpi_pixel_moved = 0
        self.dpi_canvas.config(bg="#E67E22")

    def update_dpi(self, event):
        if self.dpi_testing:
            self.dpi_pixel_moved = abs(event.x - self.dpi_start_x)

    def end_dpi(self, event):
        if not self.dpi_testing: return
        self.dpi_testing = False
        self.dpi_canvas.config(bg="#D5D8DC")
        if self.dpi_pixel_moved < 50:
            messagebox.showwarning("无效测量", "移动距离太短，请确保划过整张纸（21cm）")
            return
        dpi_val = int(self.dpi_pixel_moved / 8.2677)
        dpi_val = max(100, min(12000, dpi_val))
        self.dpi_measurements.append(dpi_val)
        n = len(self.dpi_measurements)
        self.dpi_progress.config(text=f"已完成 {n}/3 次")
        self.dpi_status.config(text=f"第{n}次：{dpi_val} DPI")
        if n >= 3:
            avg = sum(self.dpi_measurements) / n
            self.dpi.set(round(avg))
            self.dpi_status.config(text=f"平均 DPI：{round(avg)}")
            self.dpi_measurements.clear()
            self.dpi_progress.config(text="测量完成！可重新测试")
        else:
            self.dpi_status.config(text=f"还剩 {3-n} 次测量")

    def manual_dpi(self):
        win = tk.Toplevel(self.root)
        win.title("手动输入 DPI")
        win.configure(bg=BG_COLOR)
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

    # ---------- 反应测试（不变） ----------
    def start_rt(self):
        self.rt_btn.config(state="disabled", text="等待绿色...", bg="#7F8C8D")
        self.root.update()
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_green)

    def show_green(self):
        self.rt_btn.config(bg="#2ECC71", text="点击！！！", state="normal")
        self.rt_start = time.time()
        self.rt_btn.config(command=self.record_rt)

    def record_rt(self):
        rt = (time.time() - self.rt_start) * 1000
        if not hasattr(self, 'rt_list'):
            self.rt_list = []
        self.rt_list.append(rt)
        self.rt_btn.config(bg="#7F8C8D", text="继续测试", command=self.start_rt)
        if len(self.rt_list) >= 5:
            avg = sum(self.rt_list) / len(self.rt_list)
            self.reaction_time.set(round(avg, 1))
            self.rt_btn.config(bg="#95A5A6", text="测试完成", state="disabled", command=None)
            messagebox.showinfo("反应测试", f"5次平均：{avg:.1f} ms")
            self.rt_list = []

    # ---------- 查询 ----------
    def query_selected(self):
        weapon = self.selected_weapon.get()
        codes = HOT_CODES.get(weapon, [("无数据", "无", "")])
        result = f"【{weapon}】所有改枪码：\n"
        for name, code, desc in codes:
            result += f"• {name}\n  码：{code}\n  说明：{desc}\n\n"
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    # ---------- 高级推荐算法 ----------
    def full_analyze(self):
        dpi_val = self.dpi.get()
        rt_val = self.reaction_time.get()
        pref_type = self.pref_type.get()
        pref_range = self.pref_range.get()
        pref_style = self.pref_style.get()
        recoil = self.pref_recoil.get()
        supp = self.pref_suppressor.get()
        hipfire = self.pref_hipfire_grip.get()
        scope = self.pref_scope.get()
        pad = self.pad_size.get()
        res = self.screen_res.get()
        sens = self.in_game_sens.get()

        # 候选枪
        candidates = list(WEAPON_DB.keys())
        if pref_type != "自动选择":
            type_map = {
                "突击步枪": ["M4A1", "AK-47", "MK47（余烬）", "MK47（鏖战）", "K437", "腾龙", "AKM（颗秒）"],
                "冲锋枪": ["MP5", "SR3M", "MK4（全自动）", "MP7（月影）"],
                "狙击步枪": ["AWM", "RM277"],
                "射手步枪": ["M700", "KC17", "ASH12", "M14", "M7"],
            }
            candidates = [w for w in type_map.get(pref_type, []) if w in WEAPON_DB]
            if not candidates:
                candidates = list(WEAPON_DB.keys())

        best = None
        best_score = -1
        for w in candidates:
            stats = WEAPON_DB[w]
            score = 0
            # DPI与反应
            if dpi_val >= 800:
                score += stats["射速等级"] * 3
            else:
                score += (6 - stats["后坐力等级"]) * 3
            if rt_val <= 200:
                if stats["type"] in ["冲锋枪", "突击步枪"]:
                    score += 8
            else:
                if stats["type"] in ["狙击步枪", "射手步枪"]:
                    score += 8
            # 距离
            if pref_range == "近距离" and stats["type"] == "冲锋枪":
                score += 12
            elif pref_range == "远距离" and stats["type"] in ["狙击步枪", "射手步枪"]:
                score += 12
            elif pref_range == "中距离" and stats["type"] == "突击步枪":
                score += 10
            if score > best_score:
                best_score = score
                best = w
        if best is None:
            best = "M4A1"

        # 从该枪的码中选择最匹配
        codes = HOT_CODES.get(best, [])
        if not codes:
            matched = ("无推荐码", "无", "请手动查询")
        else:
            # 多条件匹配打分
            best_match = codes[0]
            best_match_score = -1
            for name, code, desc in codes:
                s = 0
                if hipfire and "腰射" in name:
                    s += 10
                if supp and "消音" in name:
                    s += 10
                if scope in ["高倍镜(6倍以上)"] and ("倍镜" in name or "高倍" in desc):
                    s += 8
                if "顶配" in name:
                    s += 2
                if pref_range == "近距离" and ("腰射" in name or "跑打" in name):
                    s += 5
                if pref_range == "远距离" and ("远射" in name or "倍镜" in name):
                    s += 5
                if s > best_match_score:
                    best_match_score = s
                    best_match = (name, code, desc)
            matched = best_match

        result = f"""【用户画像】
DPI：{dpi_val}  |  反应时间：{rt_val} ms
偏好武器：{pref_type}  |  距离：{pref_range}  |  风格：{pref_style}
压枪习惯：{recoil}  |  瞄具：{scope}
消音：{'是' if supp else '否'}  |  腰射握把：{'是' if hipfire else '否'}
鼠标垫：{pad}  |  分辨率：{res}  |  游戏灵敏度：{sens}

【智能推荐枪械】
枪械：{best} ({WEAPON_DB[best]['type']})
特点：{WEAPON_DB[best]['适合']}

【最佳匹配改枪码】
改装名称：{matched[0]}
改枪码：{matched[1]}
适用说明：{matched[2]}
（来自聪聪实测方案）
"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponAdvisorPro(root)
    root.mainloop()
