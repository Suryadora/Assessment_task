import json
import sys

def calculate_credit_rating(mortgs):
	try:
		total_risk_score = 0
		total_cred_scr = 0
		num_mortgs = len(mortgs)
		
		if num_mortgs == 0:
			raise ValueError("Mortgage list is Empty.")
		
		for mortgage in mortgs:
			ness_keys = ["credit_score", "loan_amount", "property_value", "annual_income", "debt_amount", "loan_type", "property_type"]
			for key in ness_keys:
				# print(f" key = {key}")
				if key not in mortgage:

					raise KeyError(f"Missing Necessary field: {key}")
			
			if mortgage["property_value"] <= 0:
				raise ValueError("Property value should be greater than Zero.")

			if mortgage["annual_income"] <= 0:
				raise ValueError("Annual income should be greater than zero.")

			risk_score = 0
	        
	        #loan-to-value
			ltv = mortgage["loan_amount"] / mortgage["property_value"]
			if ltv > 0.9:
				risk_score += 2
			elif ltv > 0.8:
				risk_score += 1
	        
	        #debt_to_income
			dti = mortgage["debt_amount"] / mortgage["annual_income"]
			if dti > 0.5:
				risk_score += 2
			elif dti > 0.4:
				risk_score += 1
	        
	        #credit_score
			credit_score = mortgage["credit_score"]
			total_cred_scr += credit_score
			if credit_score >= 700:
				risk_score -= 1
			elif credit_score < 650:
				risk_score += 1
	        
	        #loan_type
			if mortgage["loan_type"] == "fixed":
				risk_score -= 1
			else:
				risk_score += 1

	        
	        #property_type
			if mortgage["property_type"] == "condo":
				risk_score += 1
	        
			total_risk_score += risk_score
	    
	    #average_credit_score
		avg_cred_scr = total_cred_scr / num_mortgs
		if avg_cred_scr >= 700:
			total_risk_score -= 1
		elif avg_cred_scr < 650:
			total_risk_score += 1
	    
	    #final rating
		if total_risk_score <= 2:
			return "AAA"
		elif 3 <= total_risk_score <= 5:
			return "BBB"
		else:
			return "C"
			
	except ZeroDivisionError as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		return f"ZeroDivisionError : {str(e)} at line no {str(exc_tb.tb_lineno)}"

	except ValueError as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		return f"ValueError: {str(e)} at line no {str(exc_tb.tb_lineno)}"

	except KeyError as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		return f"KeyError: {str(e)} at line no {str(exc_tb.tb_lineno)}"




# m = {"credit_score": 750, "loan_amount": 200000, "property_value": 250000, "annual_income": 60000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"},
# print(calculate_credit_rating(m))