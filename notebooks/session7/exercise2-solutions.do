use "exercise2-data.dta", clear

twoway (line AMZN Date) (line MSFT Date) (line GME Date)

reg AMZN MSFT
reg AMZN GME

gen nAMZN = AMZN / AMZN[1]
gen nMSFT = MSFT/ MSFT[1]
nGME = GME / GME[1]

twoway (line nAMZN Date) (line nMSFT Date) (line nGME Date)

