#!/usr/bin/env python3
"""
大模型测试问题库
包含各种类型的问题，用于并发压测
"""

import random
from typing import List, Dict

class QuestionBank:
    """问题库类"""
    
    def __init__(self):
        self.questions = {
            # 知识问答类
            "knowledge": [
                "什么是人工智能？请详细解释其发展历史和主要应用领域。",
                "解释量子计算的基本原理及其与传统计算的区别。",
                "请介绍区块链技术的工作原理和主要应用场景。",
                "什么是深度学习？它与机器学习有什么区别？",
                "解释相对论的基本概念和爱因斯坦的主要贡献。",
                "请介绍DNA的结构和功能，以及基因工程的应用。",
                "什么是可持续发展？列举几个实现可持续发展的方法。",
                "解释全球变暖的原因和影响，以及应对措施。",
                "请介绍人类大脑的基本结构和功能。",
                "什么是5G技术？它比4G有哪些优势？"
            ],
            
            # 推理分析类
            "reasoning": [
                "如果一个城市的人口每年增长5%，现在有100万人，10年后会有多少人？",
                "一个房间里有3个开关，控制隔壁房间的3盏灯。你只能进入隔壁房间一次，如何确定每个开关控制哪盏灯？",
                "有5个海盗分100个金币，按资历排序投票分配。如何分配才能让提案通过？",
                "在一个岛上，有红眼睛和蓝眼睛的人，他们不知道自己的眼睛颜色。如果有外人说岛上至少有一个红眼睛的人，会发生什么？",
                "一个水池有进水管和出水管，单独开进水管需要3小时装满，单独开出水管需要5小时排空。如果两个管同时开，需要多长时间装满？",
                "如果今天是星期三，那么100天后是星期几？",
                "A比B跑得快，B比C跑得快，C比D跑得快。如果A和C比赛，A和D比赛，B和D比赛，谁会赢？",
                "一个正方形被分成4个相等的小正方形，每个小正方形再被分成4个更小的正方形。总共有多少个正方形？",
                "如果所有的A都是B，所有的B都是C，那么所有的A都是C吗？请解释逻辑推理过程。",
                "一个班级有30个学生，至少有多少个学生的生日在同一个月？"
            ],
            
            # 创作任务类
            "creative": [
                "写一篇关于未来城市的科幻小说开头，要求包含悬疑元素。",
                "创作一首关于春天的现代诗，要求韵律优美，意境深远。",
                "设计一个创新的手机APP概念，解决现代人的某个生活问题。",
                "编写一个关于人工智能觉醒的微小说，不超过200字。",
                "创作一个儿童故事，主角是一只会说话的小兔子。",
                "设计一个环保主题的广告文案，要求有创意且有感染力。",
                "写一段关于大学生活的回忆录，要求真实感人。",
                "创作一个关于时间旅行的短剧本，包含对话和场景描述。",
                "设计一个独特的节日庆祝活动方案，要求有创新性。",
                "写一篇关于友谊的散文，要求情感真挚，语言优美。"
            ],
            
            # 编程问题类
            "programming": [
                "用Python实现一个简单的计算器，支持加减乘除运算。",
                "编写一个函数来判断一个字符串是否是回文串。",
                "实现一个简单的排序算法，比如冒泡排序或快速排序。",
                "用递归方法计算斐波那契数列的第n项。",
                "编写一个程序来查找数组中的最大值和最小值。",
                "实现一个简单的链表数据结构及其基本操作。",
                "编写一个函数来检查两个字符串是否是字母异位词。",
                "用Python实现一个简单的猜数字游戏。",
                "编写一个程序来计算一个数的阶乘。",
                "实现一个简单的栈数据结构及其基本操作。"
            ],
            
            # 数学问题类
            "mathematics": [
                "求解方程 2x + 3y = 12 和 x - y = 1 的解。",
                "计算圆的面积，如果半径是5厘米。",
                "什么是素数？列举出前10个素数。",
                "解释概率的基本概念，并计算投掷硬币两次都是正面的概率。",
                "计算一个边长为4的正方形的对角线长度。",
                "什么是平均数、中位数和众数？用例子说明。",
                "计算复利：本金1000元，年利率5%，3年后的本息和。",
                "解释三角函数的基本概念，sin、cos、tan的定义。",
                "计算一个长方体的体积，长5cm，宽3cm，高2cm。",
                "什么是黄金比例？它在自然界中有哪些应用？"
            ],
            
            # 翻译任务类
            "translation": [
                "将以下英文翻译成中文：'The future belongs to those who believe in the beauty of their dreams.'",
                "将'人工智能正在改变我们的生活方式'翻译成英文。",
                "翻译这句法语：'La vie est belle'",
                "将'学而时习之，不亦说乎'翻译成现代白话文。",
                "翻译英文：'Actions speak louder than words.'",
                "将'科技让生活更美好'翻译成英文。",
                "翻译这句日语：'ありがとうございます'",
                "将'Where there is a will, there is a way'翻译成中文。",
                "翻译古文：'三人行，必有我师焉'",
                "将'Knowledge is power'翻译成中文，并解释其含义。"
            ],
            
            # 总结分析类
            "summary": [
                "总结一下COVID-19疫情对全球经济的影响。",
                "分析电商发展对传统零售业的冲击和机遇。",
                "总结人工智能在医疗领域的应用现状和前景。",
                "分析气候变化对农业生产的影响及应对策略。",
                "总结远程办公的优势和挑战。",
                "分析新能源汽车产业的发展趋势。",
                "总结移动支付对人们生活的改变。",
                "分析在线教育的发展现状和未来趋势。",
                "总结大数据技术在城市管理中的应用。",
                "分析共享经济模式的优缺点。"
            ],
            
            # 生活建议类
            "advice": [
                "作为一个大学生，如何平衡学习和社交生活？",
                "如何培养良好的时间管理习惯？",
                "给刚入职场的年轻人一些建议。",
                "如何保持身心健康的生活方式？",
                "如何提高学习效率？",
                "如何处理人际关系中的冲突？",
                "如何培养阅读习惯？",
                "如何在工作中保持创新思维？",
                "如何制定和实现个人目标？",
                "如何应对工作压力？"
            ]
        }
    
    def get_random_question(self) -> Dict[str, str]:
        """获取随机问题"""
        category = random.choice(list(self.questions.keys()))
        question = random.choice(self.questions[category])
        return {
            "category": category,
            "question": question,
            "content": question  # 用于API请求的content字段
        }
    
    def get_questions_by_category(self, category: str) -> List[str]:
        """根据类别获取问题"""
        return self.questions.get(category, [])
    
    def get_random_questions(self, count: int) -> List[Dict[str, str]]:
        """获取指定数量的随机问题"""
        questions = []
        for _ in range(count):
            questions.append(self.get_random_question())
        return questions
    
    def get_all_categories(self) -> List[str]:
        """获取所有问题类别"""
        return list(self.questions.keys())
    
    def get_total_questions_count(self) -> int:
        """获取总问题数量"""
        return sum(len(questions) for questions in self.questions.values())

# 全局问题库实例
question_bank = QuestionBank()

if __name__ == "__main__":
    # 测试问题库
    print("🎯 大模型测试问题库")
    print("=" * 50)
    
    print(f"📊 总问题数: {question_bank.get_total_questions_count()}")
    print(f"📋 问题类别: {', '.join(question_bank.get_all_categories())}")
    
    print("\n🔍 随机问题示例:")
    for i in range(5):
        q = question_bank.get_random_question()
        print(f"{i+1}. [{q['category']}] {q['question']}") 