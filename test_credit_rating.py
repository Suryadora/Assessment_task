import unittest
from credit_rating import calculate_credit_rating

class TestCreditRating(unittest.TestCase):
    def test_valid_aaa(self):
        mortgages = [
            {"credit_score": 750, "loan_amount": 200000, "property_value": 250000, "annual_income": 60000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"},
            {"credit_score": 720, "loan_amount": 150000, "property_value": 200000, "annual_income": 50000, "debt_amount": 15000, "loan_type": "fixed", "property_type": "single_family"}
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")
    
    def test_valid_bbb(self):
        mortgages = [
            {"credit_score": 675, "loan_amount": 170000, "property_value": 190000, "annual_income": 55500, "debt_amount": 25000, "loan_type": "adjustable", "property_type": "condo"},
            {"credit_score": 690, "loan_amount": 170000, "property_value": 210000, "annual_income": 50000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"}
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")
    
    def test_valid_c(self):
        mortgages = [
            {"credit_score": 640, "loan_amount": 260000, "property_value": 175000, "annual_income": 45000, "debt_amount": 30000, "loan_type": "adjustable", "property_type": "condo"},
            {"credit_score": 620, "loan_amount": 205000, "property_value": 212000, "annual_income": 30000, "debt_amount": 38000, "loan_type": "adjustable", "property_type": "condo"}
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")
    
    def test_missing_fields(self):
        mortgages = [
            {"credit_score": 750, "property_value": 250000, "annual_income": 60000, "loan_type": "fixed", "property_type": "single_family"}  # Missing debt_amount
        ]
        self.assertTrue("Error" in calculate_credit_rating(mortgages))
    
    def test_invalidvalues(self):
        mortgages = [
            {"credit_score": 600, "loan_amount": 0, "property_value": 0, "annual_income": 0, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"}  # Invalid property_value
        ]
        self.assertTrue("Error" in calculate_credit_rating(mortgages))
    
    def test_empty_list(self):
        self.assertTrue("Error" in calculate_credit_rating([]))


if __name__ == "__main__":
    unittest.main()
