sysuse auto

// Transfer Data using sfi

python:
from sfi import Data
import pandas as pd
import numpy as np
data = Data.getAsDict(['price', 'weight'], missingval=np.nan)
data = pd.DataFrame(data)
data
end

//Run Regression in StatsModels

python:
import statsmodels.formula.api as smf
results = smf.ols("weight ~ price", data=data).fit()
print(results.summary())
end

// Run Regression in Stata

reg weight price


// Option 2: Via Files

clear

sysuse auto
save "auto.dta", replace

python:
import pandas as pd
data = pd.read_stata("auto.dta")
data
end

// Run Regression in Statsmodels

python:
import statsmodels.formula.api as smf
results = smf.ols("weight ~ price", data=data).fit()
print(results.summary())
end
