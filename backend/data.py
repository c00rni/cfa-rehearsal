import json

data = {"items" : [
	{
		"statement":"A client invests €20,000 in four-years cerfificate of deposit (CD) taht annually pays interest of 3.5%. The annual CD interest payments are automatically reinvested in separate savings account at astated annual interest rate of 2% compounded monthly. At maturity, the value of the combined asset is closest to:",
		"candidates": ["A. 21,670.","B. 22,890.","C. 22,950."],
		"awnser": 1,
		"difficulty_level": 5,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"Given a stated annual interest rate of 6% compounded quartely, the level amount that, deposited qurterly, will grow to $25,000 at the end of 10 years is closest to:",
		"candidates": ["A. 461.","B. 474.","C. 836."],
		"awnser": 0,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"A sports car, purchased fro $200,000, is financed for fice years at an annual rate of 6% compounded monthly. If the first paymet is due in one month, the monthly payment is closest to:",
		"candidates": ["A. $3,847.","B. 3,867.","C. 3,957."],
		"awnser": 1,
		"difficulty_level": 5,
		"cfa_level": 1,
		"topic": 0
	},

	{
		"statement":"An investment of €500,000 today that grows to €800,000 after six years has a stated annual interest rate closest to:",
		"candidates": ["A. 7.5% compounded continuously","B. 7.7% compounded daily","C. 8.0% compounded continuously."],
		"awnser": 2,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0
	},

	{
		"statement":"For a lump sum investment of $250,000 invested at a stated annual rate of 3% compounded daily, the number of months needed to grow the sum to $1,000,000 is closest to:",
		"candidates": ["A. 555.","B. 563.","C. 576."],
		"awnser": 0,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0
	},

	{
		"statement":"A perpetual preferred stock makes its first qurartely dividend payment of $2.00 in fice quarters. If the required annual rate of return is 6% compounded quarterly the stock's present value is closest to:",
		"candidates": ["A. $31.","B. 126.","C. 133."],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0
	},

	{
		"statement": """ The present value (PV) of an investment with the following year-end cash flows (CF) and a 12% required annual rate of return is closest to: 
		
| Year     | Cash Flow € |
|----------|:-----------:|
| 1 |  100,000 |
| 2 |  150,000 |
| 3 | -10,000 |
		""",
		"candidates": ["A. ","B. ","C. "],
		"awnser": 0,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 0
	},
	{
		"statement":"Grandparents are funding a newborn's future university tuition cost, estimated at $50,000/year for four years, with the first payment due as a lump sum in 18 years. Assumming a 6% effective annual rate, the required deposit today is closest to:",
		"candidates": ["A. $60,699.","B. $64,341.","C. $68,201."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0
	},
	{
		"statement":"At a 5% interest rate per year compounded annually, the present value (PV) of a 10 year ordinary annuity with annual payments of $2,000 is $15,443,.47. The PV of a 10-year annuity due with the same interest rate an payments is closest to:",
		"candidates": ["A. $14,708.","B. $16,216.","C. $17,443."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0
	},
	{
		"statement":"A client requires €100,000 one year from now. If the stated annual rate is 2.5% compounded weekly the deposit needed today is closet to:",
		"candidates": ["A. €97,500.","B. €97,532.","C. €97,561."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0
	},
	{
		"statement":"The value in six year of $75,000 invested today at a stated annual interest reat of 7% compounded quartely is closest to:",
		"candidates": ["A. $112,555.","B. $113.330.","C. $113.733."],
		"awnser": 2,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 0
	},
	{
		"statement":"""The following exhibit shows the annual MSCI world index total returns for a 10-year period
| year 1  | 15.25%  | Year 6  | 30.79% |
| year 2  | 10.02%  | Year 7  | 12.34%  |
| year 3  | 20.65%  | Year 8  | -5.02%  |
| year 4  | 9.57%  |  Year 9 | 16.54%  |
| year 5  | -40.33%  | Year 10  | 27.37%  |
		For year 6-Year 10, the mean absolute deviation of the MSCI World Index total returns is closest to:
		""",
		"candidates": ["A. 10.20%","B. 12.74%","C. 16.40%"],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"Data values that are categorical and not amenable to being organized in a logical order are most likely to be characterized as:",
		"candidates": ["A. ordianal data.","B. discrete data.","C. nominal data."],
		"awnser": 2,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"Himari fukumoto has joined a new firm ans is selecting mutual funds in the firm's pension plan. If 10 mutual funds are available, and she plans to select four how many different sets o mutual funds can she choose ?",
		"candidates": ["A. 210","B. 720","C. 5,040"],
		"awnser": 0,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"From an approved list of 25 funds, a portfolio manager wants to rank 4 mutual funds from most recommended to least recommended. Which formula is most appropriate to calculate the number of possible ways the funds could be ranked",
		"candidates": ["A. Permutation formula","B. Multinomial formula","C. Combination formula"],
		"awnser": 0,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"A firm will select two of four vice presidents to be added to the investment comittee. How many different groups of two are possible",
		"candidates": ["A. 6","B. 12","C. 24"],
		"awnser": 0,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"An Analyst estimates that 20% of high-risk bonds will fail (go bankrupt). If she applies a bankruptcy prediction model, she finds that 70% of the nonds will receive a 'good' rating, implying that they are less likely to fail. Of the bonds that failed only 50% had a g'good' rating. (Hint, let P(A) be the probability of failure, P(B) be the probability of a 'good' rating, P(B|A) be the likelihood of a 'good' rating given failure, and P(A|B) be the likelihood of failure, and P(A|B) be the likelihood of failure given a 'good' rating.",
		"candidates": ["A. 5.7%","B. 14.3%","C. 28.6%"],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"Which of the following statements is most accurate? if the coraviance of returns between two assets is 0.0023 then:",
		"candidates": ["A. the assets' risk is near zero","B. the asset returns are unrelated","C. the asset returns have a positive relationship"],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"All else being equal, as the correlation between two assets approaches +1.0, the diversification bebefits:",
		"candidates": ["A. decrease","B. stay the same.","C. increase."],
		"awnser": 0,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"After six months, the growth portfolio that Rayan Khan manages has outperformd its benchmark. Khan states that his odd of beating the benchmark for the year are 3 to 1. if these odds are correct, what is the probability that Khan's portfolio will beat the benchmark for the year ?",
		"candidates": ["A. 0.33","B. 0.67","C. 0.75"],
		"awnser": 2,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"It the probability that Zolaf company sales exceed last year's sales is 0.167, the odds for exceeding sales are closest to:",
		"candidates": ["A. 1 to 5","B. 1 to 6","C. 5 to 1"],
		"awnser": 0,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"Which parameter equals zero in a normal distribution ?",
		"candidates": ["A. Kurtosis","B. Skewness","C. Standard deviation"],
		"awnser": 1,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"A portfolio has an expected return of 7%, with a standard deviation of 13%. For an investor with a minimum annual return target of 4%, the probability that the porfolio return will fail to meet the target is closest to:",
		"candidates": ["A. 33%","B. 41%","C. 59%"],
		"awnser": 1,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"Which of the following assets most likely requireds the use of multivariate distribution for modeling returns ?",
		"candidates": ["A. A call option on a bond.","B. A portfolio of technology stocks.","C. A stock in a market index."],
		"awnser": 1,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"A call option on a stock index is valued using a three-step binomical tree with an up move that equals 1.05 and down move that equals 0.95. The current level of the index is $190, and the option exercice price is $200. If the option value is positive when the stock price exceeds the exercise price at expiration and $0 otherwise , the number of terminal nodes with a positive payoff is:",
		"candidates": ["A. one.","B. two.","C. three."],
		"awnser": 0,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"Which of the following events can be represented as a Bernoulli trial",
		"candidates": ["A. The flip of coin","B. The closing price of a stock","C. The picking of a random integer between 1 and 10"],
		"awnser": 0,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"A portfolio manager annully ouperforms her benchmark 60% of the time. Assuming independent annual trials, what is the probabilit thatshe will outperform her benchmark four or more time over the next five ydars",
		"candidates": ["A. 0.26","B. 0.34","C. 0.48"],
		"awnser": 1,
		"difficulty_level": 5,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"Suppose we take a random sample of 30 compagnies in a industry with 200 companies. We calculate the sample mean of the ratio of cash flow to toal debt for the prior year. We find that this ratio is 23%. Subsequently, we learn that the population cash flow to total debt ratio (taking account of all 200 companies) is 26%. What is the explanation for the discrepancy between the sample mean of 23% and the population mean of 26% ?",
		"candidates": ["A. Sample error.","B. Bias.","C. A lack of consistency."],
		"awnser": 0,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"A population has a non-normal distribution with mean μ and variance σ2. The sampling distribution of the sample mean computed from samples of large size from the pupulation will have;",
		"candidates": ["A. the same distribution as the population distribution.","B. its mean approximately equal to the population mean.","C. its variance approximately equal to the population variance."],
		"awnser": 1,
		"difficulty_level": 5,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"A sample mean is computed form a pupulation with a variance of 2.45. The sample size is 40. The standard error of teh sample mean is closet to:",
		"candidates": ["A. 0.039","B. 0.247","C. 0.387"],
		"awnser": 0,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"When making a decision about investments involving a statiscally significant result, the:",
		"candidates": ["A. economic result should be presumed to be meaningful.","B. statiscal result should take priority over economic considerations.","C. economic logic for the future relevance of the result should be further explored."],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"In the step 'stating a decision rule' in testing a hypothesis, which of the following elements must be specified ?",
		"candidates": ["A. Critical value","B. Power of a test","C. Value of a test statistic"],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},
	{
		"statement":"An analyst is examining the monthly returns for two funds over one year. Both funds returns are non-normally distributed. To test whether the mean return of one fund is greater than the mean return of the other fund, the analyst can use:",
		"candidates": ["A. a parametic test only.","B. a nonparametric test only.","C. The test validity depends on manx assumptions about the nature of the population."],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},

	{
		"statement":"Homoskedasticity is best described as the situation in with the variance of the residuals of a regression is:",
		"candidates": ["A. zero.","B. normally distributed.","C. constant across observations"],
		"awnser": 2,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 0,
	},





	{
		"statement":"Which of the following statement is correct ?",
		"candidates": ["A. The appropriate tax rate to use in the adjustment of the before tax cost of debt to determine the after-tax cost of debt is the average tax rate because interest is deductible against the company's entire taxable income","B. For a given company the after-tax cost of debt is generally less than both the cost of the preferred equity and the cost of common equity.","C. For a given company, the after-tax cost of debt is generally higher than both the cost of preferred equity and the cost of common equity."],
		"awnser": 1,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"The Gearing Company has an after-tax cost of debt capitat of 4%, a cost of preferred stock of 8%, a cost of equity capital o 10% and weighted average cost of capotal of 7%. Gearing intentds to maintain its current capital structure as it raises additional capital. In making its capital-budgeting decisions for the average-risk project, the revelant costof capital is:",
		"candidates": ["A. 4%","B. 7%","C. 8%"],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Dot.com has determined that it could issue $1,000 face bonds with an 8% coupon paid semi-annually and five-year maturity at $900 per bond. if Dot.com's marginal tax is 38%, it's after-tax cost of debt is closest to:",
		"candidates": ["A. 6.2%.","B. 6.4%","C. 6.6%."],
		"awnser": 2,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Morgan Insurance Ltd. issued a fixed-rate perpetual preferred stock three years ago and placed it privately with institutional investors. The stock was issued at $25 per share with a $1.75 dividend. If the company were issue preferred sotck today, the yield would be 6.5% the stocks current value is:",
		"candidates": ["A. $25.00.","B. $26.92.","C. $37.31"],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Brandon Wiene is  financial analyst covering the beverage industriy. He is evaluating the inport of DEF Beverage's new product line of flavored waters. DEF currently has to equitity ratio of 0.6. The New product line would be financed with $50 million of debt and $100 million of equity. In estimating the valuation impact of this new product line on DEF's value, Wiene has estimated the equity beta and asset beta of comparable companies. In calculating the equity beta for the product line, Wiene is intending to use DEF's existing capital structure when converting the asset beta. Which of the following statements is a correct ?",
		"candidates": ["A. Using DEF's debt-to-equity ratio of 0.6 is appropriate in calculating the new product line's equity beta.","B. Using DEF's debt-to-equity ratio of the new product, 0.5, is appropriate to use in calculating the new product, 0.5, is appropriate to use in calcuting the new product line's equity beta.","C. Weine should use the new debt-to-equity ratio of DEF taht would result from the additional $50 million debt and $100 million equity in calculating the new product line's equity beta."],
		"awnser": 1,
		"difficulty_level": 5,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Wang Sercurities had a log -term stabel debt-to-equity ratio of 0.65. Recent bak borrowing for expension into South America raised the ratio to 0.75. The increase leverage has what effect on the asset beta and equity beta of the company ?",
		"candidates": ["A. The asset beta and equity beta will both rise.","B. The asset beta will remain the same, and the equity beta will rise","C. The asset beta will remain the same, and the equity beta will decline."],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"The weighted average cost of capital (WACC) for Van der Welde is 10%. THe company announces a debt offering taht raises the WACC to 13%. The most likely conclusion is that for Van der Welde:",
		"candidates": ["A. the company's propects are improving.","B. equity financing is cheaper than debt financing.","C. the company's debt/equity as moved beyond the optimal range."],
		"awnser": 2,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},
	{
		"statement":"According to the static trade-off theory:",
		"candidates": ["A. debt should be used only as a last resort.","B. companies have an optimal level of debt.","C. the capital structure decision is irrelevant."],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Other factors being equal, in which of the following situations are debt-equity conflicts likely to arise ?",
		"candidates": ["A. Financial leverage is low.","B. The company's debt is secured.","C. The company's debt is long-term."],
		"awnser": 2,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Which of follwing is least likely to be true with respect to angy cost and senior management compensation ?",
		"candidates": ["A. Equity-based incentive compensation is the primary method to address the problem of agency costs.","B. A well-designed compensation scheme should eliminate agency cost.","C. High cash compensation for senior management, without signficant equity-based performance inventives, can lead to excessive caution ad complancency."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Which of the following is least accurate with respect to the market value and book value of a company's equity ?",
		"candidates": ["A. Market value is more relevant than book value when measuring a company's cost of capital.","B. Book value is often used by lenders and in financial ratio calculations.","C. Both market value and book value fluctuate with change in company's share price."],
		"awnser": 2,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 3,
	},
	{
		"statement":"If two companies have identical unit sales volume and operating risk, they are most likely to also have identical:",
		"candidates": ["A. sales risk.","B. business risk.","C. sensitivity of operating earning to changes in the number of units produced ans sold."],
		"awnser": 2,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Degree of operating leverage is best described as a measure of the sensitivity of:",
		"candidates": ["A. net earnings to changes in sales.","B. fixed operating costs to changes in variables costs.","C. operating earnings to changes in the number of units produced ans sold."],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"The business risk of particular company is most accurately measured by the company's:",
		"candidates": ["A. debt-to-equity ratio.","B. effciency in using assets to generate sales.","C. operating leverage and level of uncertainty about demand, output prices, and competition."],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 3,
	},

	{
		"statement":"Consider two compamies that operate in the same line of business and have the same degree of operating leverage: The Basic Company and the Grundlegend Company. The basic Company and the Grundlegend Company have , respectively, no debt and 50 percent debt in their capital structure. Which of the following statements is most accurate ? Compared to the Basic Company, the Grundlegend Company has:",
		"candidates": ["A. a lower sensitivity of net income to changes in unit sales.","B. the same sensitivity of operating income to changes in unit sales.","C. the same sensitivty of net income to changes in operating income."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 3,
	},
	{
		"statement":"A financial analyst is examining whether a country's financial market is well functionning. She finds that the transaction costs in the market are low and trading volumes are high. She concludes that the market is quite liquid. In such a market:",
		"candidates": ["A. taders will find hard to make use of their information.","B. traders will find it easy to trad and their trading will make the market less informationally efficent.","C. traders will find it easy to trade and their trading will make the market more informationally efficent."],
		"awnser": 0,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 1,
	},

	{
		"statement":"A German publicly traded company, to raise new capital, gave it exiting share-holders the opportunity to subscibe to new shares. The existing shareholders could purchase two new shares at a subscription price of €4.58 per share for every 15 share held. this is an example of a(n):",
		"candidates": ["A. rights offering.","B. private placement.","C. Inital public offering"],
		"awnser": 2,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"A british company lised on AIM (formerly the alternative investment Market) of the London Stock Exchange announced the sale of 6,686,665 shares to a small group of qualified investors at $0.025 per share. Which of the following best describes the sales ?",
		"candidates": ["A. Shelf registration.","B. Private placement.","C. Initial public offering."],
		"awnser": 0,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 4,
	},
	{
		"statement":"""Consider the following limit order book for a stock. The bid and ask sizes are number of shares in hundreds.
| Bid Size   | Limit Price (€)  |  Offer Size |
|----------|:-------------:|------:|
| 3 |  122.80 |  |
| 8 |   123.00   |  |
| 4 | 123.35 |  |
|  | 123.80 | 7 |
|  | 124.10 | 6 |
|  | 124.50 | 7 |
A new buy limit orger is placed for 300 shares at €123.40. This limit orger is said to:
		""",
		"candidates": ["A. take the market.","B. make the market.","C. make a new market."],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"An online brokerage firm has set the minimum margin requirement at 55 percent. What is the maximum leverage ratio associated with a prosition financed by the minimum margin requirement ?",
		"candidates": ["A. 1.55.","B. 1.82.","C. 2.22."],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"A security market index represents the:",
		"candidates": ["A. risk of security market.","B. security market as a whole.","C. security market, market segmetn, or asset class."],
		"awnser": 2,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 4,
	},
	{
		"statement":"One month after inception, the price return version and total return verison of a single index (consisting of identical securities and weights) will be equal if:",
		"candidates": ["A. market prices have no changed.","B. capital gains are offset by capital losses.","C. the securities do not pay dividends or interest."],
		"awnser": 2,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Security market indexes are used as:",
		"candidates": ["A. measures of investment returns.","B. proxies to measure unsystematic risk","C. proxies for specific asset classes in asset allocation models."],
		"awnser": 2,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Reconstitution of security market index reduces:",
		"candidates": ["A. portfolio turnoever.","B. the need for rebalancing.","C. the likelihood that the index includes securities that are not representative of the target market."],
		"awnser": 2,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Which of the following index weighting methods requires the most frequent rebalancing ?",
		"candidates": ["A. Price turnover.","B. the need for rebalancing.","C. the likelihood that the index includes securites that are not representative of the target market."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"The returns of hedge fund indexes are most likely:",
		"candidates": ["A. biased upward.","B. biased downward.","C. similar across different index providers."],
		"awnser": 0,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"A unique feature of hedge fun indexes is taht they:",
		"candidates": ["A. are freqently equal weighted.","B. are deternined by the consituents of the index.","C. reflect the value of private rather than public investments."],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Which of the following is not a reat estate index category ?",
		"candidates": ["A. Appraisal index.","B. Initial sales index.","C. Repeat sales index."],
		"awnser": 1,
		"difficulty_level": 4,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Regulation that restricts some investors form participating in a market will most likely:",
		"candidates": ["A. impede market efficency.","B. not affect market efficiency.","C. contribute to market efficiency."],
		"awnser": 0,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 4,
	},
	{
		"statement":"If prices reflect all public and private information, the market is best describes the semi-strong form of market efficiency ?",
		"candidates": ["A. weak-form.","B. strong-form efficient.","C. semi-strong-form efficient."],
		"awnser": 1,
		"difficulty_level": 1,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Which of the following is least likely to explain the Janary effect anomaly ?",
		"candidates": ["A. Tax-loss selling.","B. Release of new information in January.","C. a strategy to produce future abnormal returns"],
		"awnser": 1,
		"difficulty_level": 2,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"With respect to rational and irrational investment decisions, the efficient market hypothesis requires:",
		"candidates": ["A. only that the market is rational.","B. that all investors make rational decisions.","C. that some investors make irrational decisions."],
		"awnser": 0,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 4,
	},

	{
		"statement":"Observed orreactions in markets can be explained by an investors's degree of:",
		"candidates": ["A. risk aversion.","B. loss aversion.","C. confidence in the market."],
		"awnser": 1,
		"difficulty_level": 3,
		"cfa_level": 1,
		"topic": 4,
	},

	# 4. Overview of equity securities
	{
		"statement":"",
		"candidates": ["A. ","B. ","C. "],
		"awnser": 0,
		"difficulty_level": 0,
		"cfa_level": 1,
		"topic": 4,
	},




	
]}

if __name__ == "__main__":
	print(data)

