import tkinter as tk
from tkinter import messagebox
from sympy import symbols, integrate, sympify, oo

def calculate_integral():
    var = symbols('x')
    expression = entry_expression.get()
    
    if integral_type.get() == "definite":
        lower_text = entry_lower.get()
        upper_text = entry_upper.get()
        
        # 处理无穷的情况
        if lower_text == "+":
            lower_limit = oo
        elif lower_text == "-":
            lower_limit = -oo
        else:
            try:
                lower_limit = float(lower_text)
            except:
                messagebox.showerror("错误", "下限输入无效，如需输入无穷请使用+或-")
                return
        
        if upper_text == "+":
            upper_limit = oo
        elif upper_text == "-":
            upper_limit = -oo
        else:
            try:
                upper_limit = float(upper_text)
            except:
                messagebox.showerror("错误", "上限输入无效，如需输入无穷请使用+或-")
                return
        
        try:
            expr = sympify(expression)
            result = integrate(expr, (var, lower_limit, upper_limit))
            messagebox.showinfo("计算结果", f"定积分结果为：{result}")
        except Exception as e:
            messagebox.showerror("错误", f"输入无效: {e}")
    else:
        try:
            expr = sympify(expression)
            result = integrate(expr, var)
            messagebox.showinfo("计算结果", f"不定积分结果为：{result} + C")
        except Exception as e:
            messagebox.showerror("错误", f"输入无效: {e}")

def show_special_rules():
    rules = "特殊输入规则：\n\n" \
            "• 使用'x'作为积分变量\n" \
            "• 乘号使用'*'（数字、字母、括号之间的乘号可省略）\n" \
            "• 次方使用'**'（例如：x**2表示x²）\n" \
            "• 除号使用'/'\n" \
            "• 圆周率用'pi'表示\n" \
            "• 三角函数直接使用sin、cos、tan等，与其表达式用空格隔开\n" \
            "  例如：sin x 或 sin (2*x+1)\n" \
            "• 对数函数：ln x（自然对数）, log(x)（10为底）\n" \
            "• 以a为底n的对数表示为'log(n, a)'\n" \
            "• 定积分的上下限如果是正无穷或负无穷，直接输入+或-\n" \
            "• 常见函数：exp(x)、sqrt(x)、abs(x)等"
    messagebox.showinfo("输入规则说明", rules)

def update_ui():
    if integral_type.get() == "definite":
        lower_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_lower.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        upper_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_upper.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    else:
        lower_label.grid_forget()
        entry_lower.grid_forget()
        upper_label.grid_forget()
        entry_upper.grid_forget()

app = tk.Tk()
app.title("积分计算器")
app.geometry("400x350")
app.resizable(False, False)

# 使用网格布局来组织UI元素
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

integral_type = tk.StringVar(value="indefinite")

# 第一行：标题
title_label = tk.Label(frame, text="积分计算器", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# 第二行：选择积分类型
type_frame = tk.Frame(frame)
type_frame.grid(row=1, column=0, columnspan=2, pady=10)
tk.Label(type_frame, text="选择积分类型:").pack(side="left", padx=5)
tk.Radiobutton(type_frame, text="定积分", variable=integral_type, value="definite", 
               command=update_ui).pack(side="left", padx=5)
tk.Radiobutton(type_frame, text="不定积分", variable=integral_type, value="indefinite", 
               command=update_ui).pack(side="left", padx=5)

# 定义积分的上下限和表达式输入框
lower_label = tk.Label(frame, text="下限:")
entry_lower = tk.Entry(frame, width=15)
upper_label = tk.Label(frame, text="上限:")
entry_upper = tk.Entry(frame, width=15)

# 表达式输入行
expr_label = tk.Label(frame, text="表达式:")
expr_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_expression = tk.Entry(frame, width=30)
entry_expression.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# 按钮区域
button_frame = tk.Frame(frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=15)
tk.Button(button_frame, text="计算", command=calculate_integral, width=10).pack(side="left", padx=10)
tk.Button(button_frame, text="输入规则", command=show_special_rules, width=10).pack(side="left", padx=10)

# 初始化UI状态
update_ui()

app.mainloop()