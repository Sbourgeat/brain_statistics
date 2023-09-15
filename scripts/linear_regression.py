
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import json
from statsmodels.stats.outliers_influence import variance_inflation_factor

# import dataset
brain = pd.read_csv("/Users/skumar/Project/PHD_work/GWAS/dataset/vol_hratio.csv", header = 0)



# Fit the ANOVA model
model_wo_sex = ols('abs_volume ~ C(DGRP) ', data=brain).fit()
model_w_sex = ols('abs_volume ~ C(DGRP) + sex ', data=brain).fit()
aic_wo_sex = model_wo_sex.aic
bic_wo_sex = model_wo_sex.bic

aic_w_sex = model_w_sex.aic
bic_w_sex = model_w_sex.bic

r2_wo_sex = model_wo_sex.rsquared
r2_w_sex = model_w_sex.rsquared

data = {'Model': ['Without Sex', 'With Sex'],
        'R2': [r2_wo_sex, r2_w_sex],
        'AIC': [aic_wo_sex, aic_w_sex],
        'BIC': [bic_wo_sex, bic_w_sex]}

df = pd.DataFrame(data)



# Create a dictionary with the results
results = {
    'anova_comparison': sm.stats.anova_lm(model_wo_sex, model_w_sex),
    'anova_without_sex': sm.stats.anova_lm(model_wo_sex),
    'anova_with_sex': sm.stats.anova_lm(model_w_sex)
}

# Create a dataframe from the dictionary
# Create a dataframe from the dictionary




#save the df as model scores.csv
df.to_csv('results/model_scores.csv')

#save results as a txt file 
"""for i in results.items():
    print(i)
"""

  # h_ratio

  # Fit the ANOVA model
model_wo_sex = ols('h_ratio ~ C(DGRP) ', data=brain).fit()
model_w_sex = ols('h_ratio ~ C(DGRP) + sex ', data=brain).fit()
aic_wo_sex = model_wo_sex.aic
bic_wo_sex = model_wo_sex.bic

aic_w_sex = model_w_sex.aic
bic_w_sex = model_w_sex.bic

r2_wo_sex = model_wo_sex.rsquared
r2_w_sex = model_w_sex.rsquared

data = {'Model': ['Without Sex', 'With Sex'],
        'R2': [r2_wo_sex, r2_w_sex],
        'AIC': [aic_wo_sex, aic_w_sex],
        'BIC': [bic_wo_sex, bic_w_sex]}

df = pd.DataFrame(data)

# Create a dictionary with the results
results = {
    'anova_comparison': sm.stats.anova_lm(model_wo_sex, model_w_sex),
    'anova_without_sex': sm.stats.anova_lm(model_wo_sex),
    'anova_with_sex': sm.stats.anova_lm(model_w_sex)
}



"""# Save the df as model_scores.csv
df.to_csv('results/model_scores_h_ratio.csv')"""

# Save results as a txt file
#save results as a txt file 
"""for i in results.items():
    print(i)"""


# create a new df where duplicates are kept and single are removed
# Find the duplicate rows
duplicates_df = brain[brain.duplicated(subset='DGRP', keep=False)]

# Print the new DataFrame

# model with interaction with sex
#model_wo_sex = ols('h_ratio ~ C(DGRP) ', data=brain).fit()
#model_w_sex = ols('h_ratio ~ C(DGRP) + sex ', data=brain).fit()
#model_interaction = ols('h_ratio ~ C(DGRP) + sex + C(DGRP):sex ', data=brain).fit()

model_wo_sex = ols('abs_volume ~ C(DGRP) ', data=brain).fit()
model_w_sex = ols('abs_volume ~ C(DGRP) + sex ', data=brain).fit()
model_only_sex = ols('abs_volume ~ sex ', data=brain).fit()
model_interaction = ols('abs_volume ~ C(DGRP) + sex + C(DGRP):sex ', data=duplicates_df).fit()


aic_wo_sex = model_wo_sex.aic
bic_wo_sex = model_wo_sex.bic

aic_w_sex = model_w_sex.aic
bic_w_sex = model_w_sex.bic

aic_inte = model_interaction.aic
bic_inte = model_interaction.bic

aic_only = model_only_sex.aic
bic_only = model_only_sex.bic

r2_wo_sex = model_wo_sex.rsquared
r2_w_sex = model_w_sex.rsquared
r2_inte = model_interaction.rsquared
r2_only = model_only_sex.rsquared

data = {'Model': ['Without Sex', 'With Sex','Only Sex', 'Interaction'],
        'R2': [r2_wo_sex, r2_w_sex, r2_only, r2_inte],
        'AIC': [aic_wo_sex, aic_w_sex, aic_only, aic_inte],
        'BIC': [bic_wo_sex, bic_w_sex,bic_only , bic_inte]}

df = pd.DataFrame(data)
print(df)

# Create a dictionary with the results
results = {
    'anova_comparison': sm.stats.anova_lm(model_wo_sex, model_w_sex, model_interaction),
    'anova_without_sex': sm.stats.anova_lm(model_wo_sex),
    'anova_with_sex': sm.stats.anova_lm(model_w_sex),
    'anova_interaction': sm.stats.anova_lm(model_interaction)
}

for i in results.items():
    print(i)

"""df.to_csv('results/model_scores_vol_interaction.csv')"""