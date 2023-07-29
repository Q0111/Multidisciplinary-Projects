import matplotlib.pyplot as plt
import numpy
width=0.14
days = ['Monday', 'Tuesday', 'Weds', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mass_organic = [10, 8, 6, 10, 12, 14, 10]
mass_paper = [10, 12, 4, 14, 8, 14, 6]
mass_glass = [10, 11, 14, 4, 8, 12, 6]
mass_metal = [11, 14, 10, 12, 14, 12, 14]
mass_plastic = [8, 12, 4, 12, 14, 4, 12]
mass_total = [49, 51, 61, 45, 78, 45, 40]
values = numpy.arange(len(days))
mass_plastic_values = [i+width for i in values]
mass_metal_values = [i+width for i in mass_plastic_values]
mass_glass_values = [i+width for i in mass_metal_values]
mass_organic_values = [i+width for i in mass_glass_values]
mass_paper_values = [i+width for i in mass_organic_values]
print(values)
plt.bar(values,mass_total,width,label='mass total')
print(mass_plastic_values)
plt.bar(mass_plastic_values,mass_plastic,width,label='mass paper')
print(mass_metal_values)
plt.bar(mass_metal_values,mass_metal,width,label='mass metal')
print(mass_glass_values)
plt.bar(mass_glass_values,mass_glass,width,label='mass glass')
print(mass_organic_values)
plt.bar(mass_organic_values,mass_organic,width,label='mass organic')
print(mass_paper_values)
plt.bar(mass_paper_values,mass_paper,width,label='mass paper')
plt.title('Daily Tracking Waste Chart')
plt.ylabel('mass of waste(kg)')
plt.xticks(values+0.5,days)
plt.legend()
plt.show()