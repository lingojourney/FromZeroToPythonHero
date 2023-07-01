class BmiCalculator:
    def __init__(self, weight_kg, height_cm):
        self.weight_kg = weight_kg
        self.height_cm = height_cm

    def calculate_bmi(self):
        height_m = self.height_cm / 100.0
        self.bmi = self.weight_kg / (height_m ** 2)
        return round(self.bmi, 2)

    def interpret_bmi(self):
        self.bmi = self.calculate_bmi()
        if self.bmi < 18.5:
            self.category = 'Underweight'
        elif self.bmi < 25:
            self.category = 'Normal weight'
        elif self.bmi < 30:
            self.category = 'Overweight'
        elif self.bmi < 35:
            self.category = 'Obesity (Class 1 - Low Risk)'
        elif self.bmi < 40:
            self.category = 'Obesity (Class 2 - Moderate Risk)'
        else:
            self.category = 'Obesity (Class 3 - High Risk)'
        return self.category

    def give_advice(self):
        self.category = self.interpret_bmi()
        height_m = self.height_cm / 100.0
        if self.category == 'Underweight':
            target_weight = 18.5 * (height_m ** 2)
            return f"For your height, your next milestone is to weigh at least {round(target_weight, 2)} kg to reach normal weight."
        elif self.category == 'Normal weight':
            min_normal_weight = 18.5 * (height_m ** 2)
            max_normal_weight = 24.9 * (height_m ** 2)
            return f"For your height, your weight is considered normal between {round(min_normal_weight, 2)} kg and {round(max_normal_weight, 2)} kg."
        elif self.category == 'Overweight':
            target_weight = 24.9 * (height_m ** 2)
            return f"For your height, your next milestone is to weigh less than {round(target_weight, 2)} kg to reach normal weight."
        else:  # all classes of obesity
            target_weight = { 
                'Obesity (Class 1 - Low Risk)': 29.9,
                'Obesity (Class 2 - Moderate Risk)': 34.9,
                'Obesity (Class 3 - High Risk)': 39.9,
            }[self.category] * (height_m ** 2)
            return f"For your height, your next milestone is to weigh less than {round(target_weight, 2)} kg to overcome {self.category.lower()}."

# Testing the function
bmi_calculator = BmiCalculator(94, 173)  # weight in kilograms, height in centimeters
bmi_result = bmi_calculator.calculate_bmi()
bmi_category = bmi_calculator.interpret_bmi()
advice = bmi_calculator.give_advice()

print(f"Your BMI is: {bmi_result}, Category: {bmi_category}")
print(advice)
