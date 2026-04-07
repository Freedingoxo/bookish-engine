from datetime import datetime
import sys
import os

# إضافة المجلد الرئيسي إلى مسار Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from soldiers.base_soldier import BaseSoldier

class ArmyExpansion:
    def __init__(self):
        self.soldiers = {}
        self._create_operations_division()
        self._create_products_division()
        self._create_marketing_division()
        self._create_sales_division()
        self._create_service_division()
        self._create_analytics_division()
        self._create_tech_division()
        self._create_security_division()
        self._create_content_division()
        self._create_logistics_division()
        self._log_creation()
    
    def _add_soldier(self, soldier_id: str, name: str, rank: str, division: str, specialty: str):
        self.soldiers[soldier_id] = BaseSoldier(name, rank, division, specialty)
    
    def _create_operations_division(self):
        soldiers = [
            ("OP-01", "Operations Commander", "Sergeant Major", "العمليات", "قيادة العمليات"),
            ("OP-02", "Daily Operations", "Staff Sergeant", "العمليات", "إدارة العمليات"),
            ("OP-03", "Task Scheduler", "Sergeant", "العمليات", "جدولة المهام"),
            ("OP-04", "Workflow Manager", "Sergeant", "العمليات", "إدارة سير العمل"),
            ("OP-05", "Process Optimizer", "Corporal", "العمليات", "تحسين العمليات"),
            ("OP-06", "Quality Control", "Corporal", "العمليات", "مراقبة الجودة"),
            ("OP-07", "Emergency Handler", "Sergeant", "العمليات", "معالجة الطوارئ"),
            ("OP-08", "Resource Allocator", "Corporal", "العمليات", "تخصيص الموارد"),
            ("OP-09", "Performance Tracker", "Private First Class", "العمليات", "تتبع الأداء"),
            ("OP-10", "Documentation Officer", "Private", "العمليات", "توثيق العمليات"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_products_division(self):
        soldiers = [
            ("PR-01", "Products Commander", "Sergeant Major", "المنتجات", "قيادة المنتجات"),
            ("PR-02", "Product Creator", "Staff Sergeant", "المنتجات", "إنشاء منتجات"),
            ("PR-03", "Product Updater", "Sergeant", "المنتجات", "تحديث منتجات"),
            ("PR-04", "Product Deleter", "Sergeant", "المنتجات", "حذف منتجات"),
            ("PR-05", "Bulk Editor", "Corporal", "المنتجات", "تعديلات جماعية"),
            ("PR-06", "Product Scanner", "Corporal", "المنتجات", "مسح منتجات"),
            ("PR-07", "Pricing Specialist", "Sergeant", "المنتجات", "تسعير منتجات"),
            ("PR-08", "Inventory Manager", "Corporal", "المنتجات", "إدارة مخزون"),
            ("PR-09", "Category Organizer", "Private First Class", "المنتجات", "تنظيم تصنيفات"),
            ("PR-10", "Product Reviewer", "Private", "المنتجات", "مراجعة منتجات"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_marketing_division(self):
        soldiers = [
            ("MK-01", "Marketing Commander", "Sergeant Major", "التسويق", "قيادة التسويق"),
            ("MK-02", "Campaign Manager", "Staff Sergeant", "التسويق", "إدارة حملات"),
            ("MK-03", "Social Media Specialist", "Sergeant", "التسويق", "وسائل التواصل"),
            ("MK-04", "Email Marketer", "Sergeant", "التسويق", "بريد إلكتروني"),
            ("MK-05", "SEO Specialist", "Corporal", "التسويق", "تحسين محركات البحث"),
            ("MK-06", "Content Creator", "Corporal", "التسويق", "إنشاء محتوى"),
            ("MK-07", "Ads Manager", "Sergeant", "التسويق", "إدارة إعلانات"),
            ("MK-08", "Influencer Liaison", "Corporal", "التسويق", "تواصل مع مؤثرين"),
            ("MK-09", "Affiliate Manager", "Private First Class", "التسويق", "تسويق بالعمولة"),
            ("MK-10", "Brand Guardian", "Private", "التسويق", "حماية علامة تجارية"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_sales_division(self):
        soldiers = [
            ("SL-01", "Sales Commander", "Sergeant Major", "المبيعات", "قيادة المبيعات"),
            ("SL-02", "Lead Generator", "Staff Sergeant", "المبيعات", "توليد عملاء"),
            ("SL-03", "Conversion Specialist", "Sergeant", "المبيعات", "تحسين تحويل"),
            ("SL-04", "Upsell Expert", "Sergeant", "المبيعات", "زيادة مبيعات"),
            ("SL-05", "Discount Manager", "Corporal", "المبيعات", "إدارة خصومات"),
            ("SL-06", "Cart Recovery", "Corporal", "المبيعات", "استرداد سلال"),
            ("SL-07", "Sales Analyst", "Sergeant", "المبيعات", "تحليل مبيعات"),
            ("SL-08", "B2B Specialist", "Corporal", "المبيعات", "مبيعات شركات"),
            ("SL-09", "Loyalty Manager", "Private First Class", "المبيعات", "إدارة ولاء"),
            ("SL-10", "Gift Card Manager", "Private", "المبيعات", "بطاقات هدايا"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_service_division(self):
        soldiers = [
            ("CS-01", "Service Commander", "Sergeant Major", "خدمة العملاء", "قيادة خدمة العملاء"),
            ("CS-02", "Support Agent", "Staff Sergeant", "خدمة العملاء", "دعم عملاء"),
            ("CS-03", "Chat Specialist", "Sergeant", "خدمة العملاء", "دردشة مباشرة"),
            ("CS-04", "Returns Processor", "Sergeant", "خدمة العملاء", "معالجة مرتجعات"),
            ("CS-05", "Complaint Handler", "Corporal", "خدمة العملاء", "معالجة شكاوى"),
            ("CS-06", "FAQ Manager", "Corporal", "خدمة العملاء", "إدارة أسئلة شائعة"),
            ("CS-07", "Voice Support", "Sergeant", "خدمة العملاء", "دعم صوتي"),
            ("CS-08", "Social Responder", "Corporal", "خدمة العملاء", "رد على تواصل اجتماعي"),
            ("CS-09", "Feedback Collector", "Private First Class", "خدمة العملاء", "جمع ملاحظات"),
            ("CS-10", "Satisfaction Tracker", "Private", "خدمة العملاء", "تتبع رضا"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_analytics_division(self):
        soldiers = [
            ("AN-01", "Analytics Commander", "Sergeant Major", "التحليلات", "قيادة التحليلات"),
            ("AN-02", "Sales Analyst", "Staff Sergeant", "التحليلات", "تحليل مبيعات"),
            ("AN-03", "Customer Analyst", "Sergeant", "التحليلات", "تحليل عملاء"),
            ("AN-04", "Product Analyst", "Sergeant", "التحليلات", "تحليل منتجات"),
            ("AN-05", "Competitor Analyst", "Corporal", "التحليلات", "تحليل منافسين"),
            ("AN-06", "Market Researcher", "Corporal", "التحليلات", "بحوث سوق"),
            ("AN-07", "Forecast Specialist", "Sergeant", "التحليلات", "تنبؤ"),
            ("AN-08", "Report Generator", "Corporal", "التحليلات", "توليد تقارير"),
            ("AN-09", "Data Cleaner", "Private First Class", "التحليلات", "تنظيف بيانات"),
            ("AN-10", "Insight Extractor", "Private", "التحليلات", "استخراج رؤى"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_tech_division(self):
        soldiers = [
            ("TC-01", "Technology Commander", "Sergeant Major", "التقنية", "قيادة التقنية"),
            ("TC-02", "API Manager", "Staff Sergeant", "التقنية", "إدارة APIs"),
            ("TC-03", "Integration Specialist", "Sergeant", "التقنية", "تكاملات"),
            ("TC-04", "Automation Engineer", "Sergeant", "التقنية", "أتمتة عمليات"),
            ("TC-05", "Database Manager", "Corporal", "التقنية", "إدارة قواعد بيانات"),
            ("TC-06", "Server Monitor", "Corporal", "التقنية", "مراقبة خوادم"),
            ("TC-07", "Security Tech", "Sergeant", "التقنية", "تقني أمن"),
            ("TC-08", "Backup Specialist", "Corporal", "التقنية", "نسخ احتياطي"),
            ("TC-09", "Speed Optimizer", "Private First Class", "التقنية", "تحسين سرعة"),
            ("TC-10", "Debugger", "Private", "التقنية", "تصحيح أخطاء"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_security_division(self):
        soldiers = [
            ("SC-01", "Security Commander", "Sergeant Major", "الأمن", "قيادة الأمن"),
            ("SC-02", "Fraud Detector", "Staff Sergeant", "الأمن", "كشف احتيال"),
            ("SC-03", "Threat Hunter", "Sergeant", "الأمن", "صيد تهديدات"),
            ("SC-04", "Access Controller", "Sergeant", "الأمن", "تحكم وصول"),
            ("SC-05", "Data Protector", "Corporal", "الأمن", "حماية بيانات"),
            ("SC-06", "Firewall Manager", "Corporal", "الأمن", "إدارة جدار حماية"),
            ("SC-07", "Penetration Tester", "Sergeant", "الأمن", "اختبار اختراق"),
            ("SC-08", "Audit Logger", "Corporal", "الأمن", "تسجيل تدقيق"),
            ("SC-09", "Compliance Officer", "Private First Class", "الأمن", "مسؤول امتثال"),
            ("SC-10", "Incident Responder", "Private", "الأمن", "استجابة حوادث"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_content_division(self):
        soldiers = [
            ("CT-01", "Content Commander", "Sergeant Major", "المحتوى", "قيادة المحتوى"),
            ("CT-02", "Blog Writer", "Staff Sergeant", "المحتوى", "كتابة مدونة"),
            ("CT-03", "Product Describer", "Sergeant", "المحتوى", "وصف منتجات"),
            ("CT-04", "SEO Writer", "Sergeant", "المحتوى", "كتابة محتوى SEO"),
            ("CT-05", "Social Copywriter", "Corporal", "المحتوى", "كتابة منشورات"),
            ("CT-06", "Email Copywriter", "Corporal", "المحتوى", "كتابة بريد"),
            ("CT-07", "Video Scriptwriter", "Sergeant", "المحتوى", "كتابة سيناريو"),
            ("CT-08", "Translator", "Corporal", "المحتوى", "ترجمة"),
            ("CT-09", "Proofreader", "Private First Class", "المحتوى", "تدقيق لغوي"),
            ("CT-10", "Content Curator", "Private", "المحتوى", "تنظيم محتوى"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _create_logistics_division(self):
        soldiers = [
            ("LG-01", "Logistics Commander", "Sergeant Major", "الخدمات اللوجستية", "قيادة الخدمات اللوجستية"),
            ("LG-02", "Shipping Manager", "Staff Sergeant", "الخدمات اللوجستية", "إدارة شحن"),
            ("LG-03", "Inventory Planner", "Sergeant", "الخدمات اللوجستية", "تخطيط مخزون"),
            ("LG-04", "Warehouse Manager", "Sergeant", "الخدمات اللوجستية", "إدارة مستودع"),
            ("LG-05", "Fulfillment Specialist", "Corporal", "الخدمات اللوجستية", "تلبية طلبات"),
            ("LG-06", "Returns Manager", "Corporal", "الخدمات اللوجستية", "إدارة مرتجعات"),
            ("LG-07", "Supplier Liaison", "Sergeant", "الخدمات اللوجستية", "تواصل مع موردين"),
            ("LG-08", "Cost Optimizer", "Corporal", "الخدمات اللوجستية", "تحسين تكاليف"),
            ("LG-09", "Tracking Specialist", "Private First Class", "الخدمات اللوجستية", "تتبع شحنات"),
            ("LG-10", "Customs Handler", "Private", "الخدمات اللوجستية", "معالجة جمارك"),
        ]
        for sid, name, rank, div, spec in soldiers:
            self._add_soldier(sid, name, rank, div, spec)
    
    def _log_creation(self):
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                 🪖 الجيش الكامل (100 جندي) 🪖                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}   ║
║   🪖 إجمالي الجنود: {len(self.soldiers)}                                       ║
║   🏢 عدد الفرق: 10                                           ║
║                                                              ║
║   ✅ الجيش جاهز للعمل                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def get_army_report(self) -> str:
        divisions = {}
        for soldier in self.soldiers.values():
            if soldier.division not in divisions:
                divisions[soldier.division] = 0
            divisions[soldier.division] += 1
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║                   📋 تقرير الجيش الكامل                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}   ║
║   🪖 إجمالي الجنود: {len(self.soldiers)}                                       ║
║                                                              ║
"""
        for div_name, count in divisions.items():
            report += f"""
║   📁 {div_name}: {count} جندي                                          ║
"""
        
        report += """
║                                                              ║
║   ✅ الجيش جاهز للعمل                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        return report

if __name__ == "__main__":
    army = ArmyExpansion()
    print(army.get_army_report())
