import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# ==================== 枪械数据库 ====================
WEAPON_DB = {
    "M4A1": {"type": "突击步枪", "适合": "均衡中距离", "后坐力": 3, "射速": 3, "伤害": 2},
    "MP5":  {"type": "冲锋枪",   "适合": "近战高速",   "后坐力": 1, "射速": 5, "伤害": 1},
    "AK-47":{"type": "突击步枪", "适合": "高伤压枪",   "后坐力": 5, "射速": 2, "伤害": 4},
    "AWM":  {"type": "狙击步枪", "适合": "一击致命",   "后坐力": 5, "射速": 1, "伤害": 5},
    "M700": {"type": "射手步枪", "适合": "灵活狙击",   "后坐力": 4, "射速": 2, "伤害": 4},
    "SR3M": {"type": "冲锋枪",   "适合": "撕咬双修",   "后坐力": 2, "射速": 4, "伤害": 2},
    "KC17": {"type": "射手步枪", "适合": "远距压制",   "后坐力": 3, "射速": 2, "伤害": 4},
    "MK47（余烬）": {"type": "突击步枪", "适合": "均衡影袭", "后坐力": 3, "射速": 3, "伤害": 3},
    "RM277": {"type": "狙击步枪", "适合": "重型高伤",   "后坐力": 4, "射速": 1, "伤害": 5},
    "AKM（颗秒）": {"type": "突击步枪", "适合": "暴力压枪", "后坐力": 5, "射速": 2, "伤害": 4},
    "ASH12": {"type": "射手步枪", "适合": "双发双修",   "后坐力": 3, "射速": 2, "伤害": 4},
    "MK4（全自动）": {"type": "冲锋枪", "适合": "全自动腰射", "后坐力": 2, "射速": 5, "伤害": 1},
    "K437": {"type": "突击步枪", "适合": "双流顶配",   "后坐力": 3, "射速": 3, "伤害": 3},
    "M14": {"type": "射手步枪", "适合": "共振系列",   "后坐力": 3, "射速": 2, "伤害": 4},
    "M7":  {"type": "射手步枪", "适合": "CT消音顶配", "后坐力": 3, "射速": 2, "伤害": 4},
    "MP7（月影）": {"type": "冲锋枪", "适合": "极限双修", "后坐力": 2, "射速": 5, "伤害": 2},
    "腾龙": {"type": "突击步枪", "适合": "双水平满改", "后坐力": 3, "射速": 3, "伤害": 3},
    "MK47（鏖战）": {"type": "突击步枪", "适合": "无后坐BUG", "后坐力": 1, "射速": 4, "伤害": 3},  # 补全缺失武器
}

# ==================== 聪聪改枪码库 ====================
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

# ==================== 三角洲行动干员数据（完整版11人） ====================
OPERATORS = {
    # ---- 突击兵 ----
    "威龙": {
        "兵种": "突击",
        "原名": "王宇昊",
        "风格": "快速突进，虎蹲炮击倒敌人，以少胜多",
        "偏好类型": "突击步枪",
        "改码关键词": ["压枪", "腰射", "均衡", "突进"]
    },
    "红狼": {
        "兵种": "突击",
        "原名": "凯·席尔瓦",
        "风格": "动力外骨骼高机动，游击战术，榴弹逆转战局",
        "偏好类型": "突击步枪",
        "改码关键词": ["稳定", "倍镜", "长管", "顶配"]
    },
    "无名": {
        "兵种": "突击",
        "原名": "埃利奥·德·蒙贝尔",
        "风格": "S4赛季上线，突击型精英",
        "偏好类型": "突击步枪",
        "改码关键词": ["压枪", "顶配", "均衡", "稳定"]
    },
    "疾风": {
        "兵种": "突击",
        "原名": "克莱儿·安·拜尔斯",
        "风格": "高机动移动，交战中提升移动与翻滚速度",
        "偏好类型": "冲锋枪",
        "改码关键词": ["跑打", "腰射", "机动", "短管"]
    },
    # ---- 支援兵 ----
    "蜂医": {
        "兵种": "支援",
        "原名": "罗伊·斯米",
        "风格": "激素手枪治疗队友，烟幕分割战场",
        "偏好类型": "冲锋枪",
        "改码关键词": ["腰射", "稳定", "性价比", "跑打"]
    },
    "蛊": {
        "兵种": "支援",
        "原名": "佐亚·庞琴科娃",
        "风格": "支援型，致盲毒雾攻楼守点",
        "偏好类型": "冲锋枪",
        "改码关键词": ["腰射", "高改", "双修", "机动"]
    },
    # ---- 侦察兵 ----
    "露娜": {
        "兵种": "侦察",
        "原名": "金卢娜",
        "风格": "侦查箭矢洞悉敌情，电击箭矢持续伤害",
        "偏好类型": "狙击步枪",
        "改码关键词": ["倍镜", "远射", "消音", "瞬狙"]
    },
    "骇爪": {
        "兵种": "侦察",
        "原名": "麦晓雯",
        "风格": "电子攻防专家，飞刀标记敌人，隐蔽追踪",
        "偏好类型": "冲锋枪",
        "改码关键词": ["消音", "腰射", "机动", "渗透"]
    },
    "银翼": {
        "兵种": "侦察",
        "原名": "兰登·哈里森",
        "风格": "猎鹰无人机追踪，蜂鸟摄像头破解情报",
        "偏好类型": "狙击步枪",
        "改码关键词": ["倍镜", "远射", "消音", "情报"]
    },
    # ---- 工程兵 ----
    "牧羊人": {
        "兵种": "工程",
        "原名": "泰瑞·缪萨",
        "风格": "声波陷阱布防，声波无人机范围压制",
        "偏好类型": "射手步枪",
        "改码关键词": ["双修", "CT", "倍镜", "共振"]
    },
    "乌鲁鲁": {
        "兵种": "工程",
        "原名": "大卫·费莱尔",
        "风格": "巡飞弹精确打击，速凝掩体防护，燃烧弹破障",
        "偏好类型": "射手步枪",
        "改码关键词": ["双修", "倍镜", "共振", "顶配"]
    },
    "深蓝": {
        "兵种": "工程",
        "原名": "阿列克谢·彼得罗夫",
        "风格": "防爆套装推进，帮助小队突破防线",
        "偏好类型": "突击步枪",
        "改码关键词": ["压枪", "稳定", "顶配", "推进"]
    },
}

# ==================== UI 配色 ====================
BG = "#F2F4F7"
CARD = "#FFFFFF"
ACCENT = "#1E293B"
BLUE = "#3B82F6"
GREEN = "#10B981"
RED = "#EF4444"


class DeltaWeaponAdvisor:
    def __init__(self, root):
        self.root = root
        self.root.title("三角洲行动 · 聪聪改枪码助手")
        self.root.geometry("720x800")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # 状态变量
        self.dpi = tk.IntVar(value=800)
        self.reaction = tk.DoubleVar(value=250.0)
        self.operator = tk.StringVar(value="威龙")

        # 测试数据
        self.dpi_measurements = []
        self.rt_list = []
        self.dpi_testing = False
        self.dpi_start = 0
        self.dpi_pixel = 0
        self.rt_start = 0

        self.build_ui()

    # ==================== UI 构建 ====================
    def build_ui(self):
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        # 标题
        title = tk.Label(main, text="三角洲行动 · 聪聪改枪码推荐",
                         font=("微软雅黑", 20, "bold"), fg=ACCENT, bg=BG)
        title.pack(pady=(0, 15))

        # 三个步骤卡片（改用网格布局，更稳定）
        step_frame = tk.Frame(main, bg=BG)
        step_frame.pack(fill="x", pady=5)

        # 卡片1：DPI测试
        card1 = tk.Frame(step_frame, bg=CARD, relief="solid", bd=1, padx=15, pady=12)
        card1.pack(side="left", fill="both", expand=True, padx=4)
        tk.Label(card1, text="① DPI 测试", font=("微软雅黑", 11, "bold"),
                 bg=CARD, fg=ACCENT).pack(anchor="w")
        self.dpi_canvas = tk.Canvas(card1, height=40, bg="#E2E8F0", highlightthickness=0)
        self.dpi_canvas.pack(fill="x", pady=8)
        self.dpi_canvas.bind("<Button-1>", self.start_dpi)
        self.dpi_canvas.bind("<B1-Motion>", self.update_dpi)
        self.dpi_canvas.bind("<ButtonRelease-1>", self.end_dpi)
        self.dpi_status = tk.Label(card1, text="按住左键，从左到右划 21cm",
                                   bg=CARD, fg="#64748B", font=("微软雅黑", 8))
        self.dpi_status.pack()
        self.dpi_label = tk.Label(card1, textvariable=self.dpi,
                                  bg=CARD, fg=RED, font=("微软雅黑", 13, "bold"))
        self.dpi_label.pack()
        tk.Button(card1, text="手动输入", bg="#CBD5E1", fg=ACCENT,
                  relief="flat", font=("微软雅黑", 9),
                  command=self.manual_dpi).pack(pady=4)

        # 卡片2：反应测试
        card2 = tk.Frame(step_frame, bg=CARD, relief="solid", bd=1, padx=15, pady=12)
        card2.pack(side="left", fill="both", expand=True, padx=4)
        tk.Label(card2, text="② 反应速度", font=("微软雅黑", 11, "bold"),
                 bg=CARD, fg=ACCENT).pack(anchor="w")
        self.rt_btn = tk.Button(card2, text="开始测试 (5次)", bg="#94A3B8",
                                fg="white", font=("微软雅黑", 10, "bold"),
                                relief="flat", padx=15, pady=8,
                                command=self.start_rt)
        self.rt_btn.pack(pady=10)
        self.rt_label = tk.Label(card2, textvariable=self.reaction,
                                 bg=CARD, fg=RED, font=("微软雅黑", 13, "bold"))
        self.rt_label.pack()

        # 卡片3：选择干员
        card3 = tk.Frame(step_frame, bg=CARD, relief="solid", bd=1, padx=15, pady=12)
        card3.pack(side="left", fill="both", expand=True, padx=4)
        tk.Label(card3, text="③ 选择干员", font=("微软雅黑", 11, "bold"),
                 bg=CARD, fg=ACCENT).pack(anchor="w")
        ops = list(OPERATORS.keys())
        self.op_combo = ttk.Combobox(card3, textvariable=self.operator,
                                     values=ops, state="readonly",
                                     font=("微软雅黑", 10))
        self.op_combo.pack(pady=8, fill="x")
        self.op_desc = tk.Label(card3, text="", bg=CARD, fg="#64748B",
                                font=("微软雅黑", 8), wraplength=170)
        self.op_desc.pack()
        self.op_combo.bind("<<ComboboxSelected>>", self.update_op_desc)
        self.update_op_desc()

        # 分析按钮
        btn = tk.Button(main, text="🔍 生成我的专属改枪码", bg=BLUE, fg="white",
                        font=("微软雅黑", 13, "bold"), relief="flat",
                        padx=30, pady=12, command=self.analyze)
        btn.pack(pady=15)

        # 结果显示
        self.result = tk.Text(main, height=14, width=80, font=("微软雅黑", 10),
                              wrap="word", bg=CARD, relief="solid",
                              bd=1, padx=15, pady=15)
        self.result.pack(fill="both", expand=True)

    # ==================== 辅助方法 ====================
    def update_op_desc(self, event=None):
        """更新干员描述"""
        op = self.operator.get()
        data = OPERATORS.get(op)
        if data:
            desc = f"兵种：{data['兵种']} ｜ {data['风格']}"
            self.op_desc.config(text=desc)

    # ==================== DPI 测试 ====================
    def start_dpi(self, event):
        self.dpi_testing = True
        self.dpi_start = event.x
        self.dpi_pixel = 0
        self.dpi_canvas.config(bg="#FCD34D")

    def update_dpi(self, event):
        if self.dpi_testing:
            self.dpi_pixel = abs(event.x - self.dpi_start)

    def end_dpi(self, event):
        if not self.dpi_testing:
            return
        self.dpi_testing = False
        self.dpi_canvas.config(bg="#E2E8F0")

        if self.dpi_pixel < 50:
            messagebox.showwarning("提示", "移动距离太短，请确保移动了约 21cm")
            return

        # 像素转 DPI（假设 21cm ≈ 8.2677 英寸）
        val = int(self.dpi_pixel / 8.2677)
        val = max(100, min(12000, val))
        self.dpi_measurements.append(val)

        n = len(self.dpi_measurements)
        if n >= 3:
            avg = sum(self.dpi_measurements) / n
            self.dpi.set(round(avg))
            self.dpi_status.config(text=f"✅ 平均 DPI：{round(avg)}")
            self.dpi_measurements.clear()
        else:
            self.dpi_status.config(text=f"第{n}次：{val} DPI（还需 {3-n} 次）")

    def manual_dpi(self):
        """手动输入 DPI"""
        win = tk.Toplevel(self.root)
        win.title("手动输入 DPI")
        win.geometry("260x150")
        win.configure(bg=BG)
        win.resizable(False, False)

        tk.Label(win, text="输入 DPI (100-12000):", bg=BG,
                 font=("微软雅黑", 10)).pack(pady=12)
        entry = ttk.Entry(win, font=("微软雅黑", 11))
        entry.pack(pady=5)
        entry.focus()

        def set_dpi():
            try:
                v = int(entry.get().strip())
                if 100 <= v <= 12000:
                    self.dpi.set(v)
                    self.dpi_measurements.clear()
                    self.dpi_status.config(text="✅ 已手动设定")
                    win.destroy()
                else:
                    messagebox.showwarning("错误", "DPI 范围：100 ~ 12000")
            except ValueError:
                messagebox.showwarning("错误", "请输入有效整数")

        tk.Button(win, text="确定", bg=BLUE, fg="white",
                  font=("微软雅黑", 10), relief="flat",
                  padx=20, pady=5, command=set_dpi).pack(pady=10)

        # 回车键绑定
        win.bind("<Return>", lambda e: set_dpi())

    # ==================== 反应测试 ====================
    def start_rt(self):
        """开始反应测试"""
        self.rt_btn.config(state="disabled", text="⏳ 等待绿色...",
                           bg="#94A3B8", command=None)
        self.root.update()
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_green)

    def show_green(self):
        """显示绿色按钮"""
        self.rt_btn.config(bg=GREEN, text="🔥 点我！", state="normal")
        self.rt_start = time.time()
        self.rt_btn.config(command=self.record_rt)

    def record_rt(self):
        """记录反应时间"""
        rt = (time.time() - self.rt_start) * 1000
        self.rt_list.append(rt)

        if len(self.rt_list) >= 5:
            avg = sum(self.rt_list) / 5
            self.reaction.set(round(avg, 1))
            self.rt_btn.config(bg="#CBD5E1", text="✅ 测试完成",
                               state="disabled", command=None)
            messagebox.showinfo("反应测试完成",
                                f"平均反应时间：{avg:.1f} ms\n\n"
                                f"👉 小于 200ms：适合冲锋/突击\n"
                                f"👉 大于 200ms：适合狙击/射手步枪")
            self.rt_list.clear()
        else:
            self.rt_btn.config(bg="#94A3B8", text=f"继续测试 ({len(self.rt_list)}/5)",
                               command=self.start_rt)

    # ==================== 核心推荐引擎 ====================
    def analyze(self):
        """生成武器推荐"""
        dpi = self.dpi.get()
        rt = self.reaction.get()
        op = self.operator.get()
        op_data = OPERATORS.get(op)

        if not op_data:
            messagebox.showwarning("错误", "请选择有效的干员")
            return

        # ---- 1. 根据干员偏好类型筛选候选枪 ----
        pref_type = op_data["偏好类型"]

        # 动态从 WEAPON_DB 按类型筛选（避免硬编码遗漏）
        candidates = [w for w, info in WEAPON_DB.items() if info["type"] == pref_type]

        if not candidates:
            # 降级：如果该类型无武器，使用全部武器
            candidates = list(WEAPON_DB.keys())
            messagebox.showwarning("提示", f"未找到 {pref_type} 类型武器，已使用全部武器")

        # ---- 2. 根据 DPI 和反应时间打分 ----
        scores = {}
        for w in candidates:
            stat = WEAPON_DB[w]
            score = 0

            # DPI 高 → 适合高射速；DPI 低 → 适合低后坐力
            if dpi >= 800:
                score += stat["射速"] * 3
            else:
                score += (6 - stat["后坐力"]) * 3

            # 反应快 → 适合冲锋/突击；反应慢 → 适合狙击/射手步枪
            if rt <= 200:
                if stat["type"] in ["冲锋枪", "突击步枪"]:
                    score += 8
            else:
                if stat["type"] in ["狙击步枪", "射手步枪"]:
                    score += 8

            scores[w] = score

        # 选出得分最高的武器
        best_weapon = max(scores, key=scores.get)

        # ---- 3. 匹配改枪码 ----
        codes = HOT_CODES.get(best_weapon, [])
        if codes:
            best_match = codes[0]
            best_score = -1
            for name, code, desc in codes:
                s = sum(10 for kw in op_data["改码关键词"] if kw in name)
                if s > best_score:
                    best_score = s
                    best_match = (name, code, desc)
        else:
            best_match = ("默认配置", "N/A", "暂无推荐改码")

        # ---- 4. 输出结果 ----
        result = f"""
╔═══════════════════════════════════════════════════════════╗
║                    📊 你的数据                           ║
╠═══════════════════════════════════════════════════════════╣
║  DPI：{dpi}  ｜  反应时间：{rt} ms  ｜  干员：{op}（{op_data['兵种']}）  ║
╚═══════════════════════════════════════════════════════════╝

【🎯 智能推荐】
  枪械：{best_weapon}（{WEAPON_DB[best_weapon]['type']}）
  特点：{WEAPON_DB[best_weapon]['适合']}

【📋 主播聪聪同款改枪码】
  改装名称：{best_match[0]}
  改枪码：  {best_match[1]}
  适用说明：{best_match[2]}
  （直接复制到游戏里导入即可）

【💡 小贴士】
  • DPI ≥ 800 推荐高射速武器；DPI < 800 推荐低后坐力武器
  • 反应 ≤ 200ms 适合冲锋突击；反应 > 200ms 适合狙击架点
"""
        self.result.delete(1.0, tk.END)
        self.result.insert(tk.END, result)


# ==================== 启动 ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = DeltaWeaponAdvisor(root)
    root.mainloop()
