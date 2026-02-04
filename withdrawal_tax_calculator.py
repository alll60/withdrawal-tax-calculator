"""
Withdrawal Tax Calculator / Calculateur d'Impôt sur Retraits
=============================================================
Bilingual (EN/FR) - Quebec resident focused - Tax Year 2025

Run with: streamlit run withdrawal_tax_calculator.py
"""

import streamlit as st

# =============================================================================
# LANGUAGE STRINGS
# =============================================================================

LANG = {
    "en": {
        "title": "Withdrawal Tax Calculator",
        "subtitle": "**Quebec Resident | Tax Year 2025**",
        "your_situation": "Your Situation",
        "annual_income": "Annual Income",
        "employment_pension": "Employment / Pension ($)",
        "employment_pension_help": "Salary, employer pension, etc.",
        "cpp_qpp": "CPP / QPP ($)",
        "cpp_qpp_help": "Canada/Quebec Pension Plan (starts age 60)",
        "oas_psv": "OAS / PSV ($)",
        "oas_psv_help": "Old Age Security (starts age 65, max ~$8,820/yr)",
        "dividends": "Dividends ($)",
        "dividends_help": "Eligible Canadian dividends (grossed-up 38%)",
        "crypto": "Crypto / Digital Assets ($)",
        "crypto_help": "Capital gains from crypto (50% taxable)",
        "other_income": "Other Annual Income ($)",
        "other_income_help": "Employment, pension, CPP/QPP, etc.",
        "account_balances": "Account Balances",
        "rrsp_balance": "RRSP/RRIF Balance ($)",
        "tfsa_balance": "TFSA Balance ($)",
        "non_reg_balance": "Non-Registered Balance ($)",
        "non_reg_acb": "Non-Reg Cost Base ($)",
        "non_reg_acb_help": "Original purchase cost (ACB)",
        "unrealized_gain": "Unrealized gain",
        "your_age": "Your Age",
        "receiving_oas": "Receiving OAS",
        "how_much_need": "How much do you need?",
        "total_cash_needed": "Total cash needed ($)",
        "split_withdrawal": "Split Your Withdrawal",
        "split_instructions": "Drag the sliders to decide how much to take from each account.",
        "tfsa": "TFSA",
        "from_tfsa": "From TFSA ($)",
        "non_reg": "Non-Registered",
        "from_non_reg": "From Non-Reg ($)",
        "rrsp": "RRSP/RRIF",
        "from_rrsp": "From RRSP ($)",
        "available": "Available",
        "results": "Results",
        "shortfall": "Shortfall",
        "shortfall_msg": "You need to withdraw more!",
        "surplus": "Surplus",
        "surplus_msg": "You're withdrawing more than needed.",
        "target_met": "Target met",
        "cash_received": "Cash Received",
        "target": "Target",
        "tax_on_withdrawals": "Tax on Withdrawals",
        "oas_clawback": "OAS Clawback",
        "na": "N/A",
        "total_cost": "Total Cost",
        "effective": "effective",
        "breakdown": "Breakdown",
        "withdrawals": "**Withdrawals**",
        "account": "Account",
        "gross": "Gross",
        "withholding": "Withholding",
        "net_received": "Net Received",
        "total": "Total",
        "tax_impact": "**Tax Impact**",
        "item": "Item",
        "amount": "Amount",
        "other_annual_income": "Other annual income",
        "rrsp_withdrawal": "RRSP withdrawal",
        "capital_gain_50": "Capital gain (50% of",
        "total_taxable_income": "Total taxable income",
        "federal_bpa": "Federal BPA (tax-free)",
        "quebec_bpa": "Quebec BPA (tax-free)",
        "dividend_tax_credit": "Dividend tax credit",
        "tax_before_credits": "Tax before credits",
        "tax_on_withdrawals_row": "Tax on withdrawals",
        "less_withholding": "Less: Withholding paid",
        "owe_at_tax_time": "Owe at tax time",
        "marginal_rate_msg": "Your marginal tax rate at",
        "income": "income",
        "income_sources": "**Income Sources**",
        "optimization_tips": "Optimization Tips",
        "tip_use_more_tfsa": "**Use more TFSA** — It's tax-free and doesn't affect OAS.",
        "tip_rrsp_triggered_clawback": "**RRSP triggered {} OAS clawback** — Consider using non-registered or TFSA instead.",
        "tip_non_reg_more_efficient": "**Non-registered is more tax-efficient** — Effective rate on gains (~{}%) is lower than RRSP ({}%).",
        "tip_over_oas_threshold": "**You're {} over OAS threshold** — Each extra $1 of taxable income costs 15¢ in clawback.",
        "target_type": "Target type",
        "total_annual_cash": "Total annual cash needed",
        "additional_cash": "Additional cash (on top of other income)",
        "withdrawal_needed": "Withdrawal needed",
        "you_already_have": "You already have {} from other income",
        "tip_looks_reasonable": "Your current mix looks reasonable!",
        "tax_reference": "Tax Reference (2025)",
        "combined_rates": "### Combined Marginal Rates (Federal + Quebec)",
        "rrsp_withholding_title": "### RRSP Withholding (Quebec)",
        "up_to": "Up to",
        "over": "Over",
        "oas_clawback_title": "### OAS Clawback",
        "starts_at": "Starts at",
        "net_income": "net income",
        "rate": "Rate",
        "of_income_over": "of income over threshold",
        "max_oas": "Max OAS (65-74)",
        "year": "year",
        "capital_gains_title": "### Capital Gains",
        "capital_gains_info": "Only 50% of gains are taxable",
        "effective_max_rate": "Effective max rate",
        "disclaimer": "Data: TaxTips.ca, Canada.ca, Revenu Québec | For educational purposes only",
        "tax_on_other_income": "Tax on other income",
        "total_annual_tax": "Total annual tax",
        "already_withheld": "Already withheld (paycheck)",
        "full_tax_picture": "**Full Tax Picture**",
        "net_annual_income": "Net Annual Income",
        "gross_income": "Gross income (other + withdrawals)",
        "less_total_tax": "Less: Total tax",
        "net_after_tax": "Net after tax",
        "download_csv": "Download Results (CSV)",
        "download_filename": "withdrawal_tax_results.csv"
    },
    "fr": {
        "title": "Calculateur d'Impôt sur Retraits",
        "subtitle": "**Résident du Québec | Année d'imposition 2025**",
        "your_situation": "Votre Situation",
        "annual_income": "Revenus annuels",
        "employment_pension": "Emploi / Pension ($)",
        "employment_pension_help": "Salaire, pension employeur, etc.",
        "cpp_qpp": "RPC / RRQ ($)",
        "cpp_qpp_help": "Régime de rentes du Québec (début à 60 ans)",
        "oas_psv": "SV / PSV ($)",
        "oas_psv_help": "Sécurité de la vieillesse (début à 65 ans, max ~8 820$/an)",
        "dividends": "Dividendes ($)",
        "dividends_help": "Dividendes canadiens déterminés (majorés de 38%)",
        "crypto": "Crypto / Actifs numériques ($)",
        "crypto_help": "Gains en capital sur crypto (50% imposable)",
        "other_income": "Autres revenus annuels ($)",
        "other_income_help": "Emploi, pension, RRQ/RPC, etc.",
        "account_balances": "Soldes des comptes",
        "rrsp_balance": "Solde REER/FERR ($)",
        "tfsa_balance": "Solde CELI ($)",
        "non_reg_balance": "Solde non enregistré ($)",
        "non_reg_acb": "Prix de base rajusté ($)",
        "non_reg_acb_help": "Coût d'achat original (PBR)",
        "unrealized_gain": "Gain non réalisé",
        "your_age": "Votre âge",
        "receiving_oas": "Reçoit la PSV",
        "how_much_need": "Combien avez-vous besoin?",
        "total_cash_needed": "Montant net requis ($)",
        "split_withdrawal": "Répartir vos retraits",
        "split_instructions": "Ajustez les curseurs pour décider combien retirer de chaque compte.",
        "tfsa": "CELI",
        "from_tfsa": "Du CELI ($)",
        "non_reg": "Non enregistré",
        "from_non_reg": "Du non enregistré ($)",
        "rrsp": "REER/FERR",
        "from_rrsp": "Du REER ($)",
        "available": "Disponible",
        "results": "Résultats",
        "shortfall": "Manque",
        "shortfall_msg": "Vous devez retirer plus!",
        "surplus": "Surplus",
        "surplus_msg": "Vous retirez plus que nécessaire.",
        "target_met": "Objectif atteint",
        "cash_received": "Montant reçu",
        "target": "Cible",
        "tax_on_withdrawals": "Impôt sur retraits",
        "oas_clawback": "Récupération PSV",
        "na": "S/O",
        "total_cost": "Coût total",
        "effective": "effectif",
        "breakdown": "Décomposition",
        "withdrawals": "**Retraits**",
        "account": "Compte",
        "gross": "Brut",
        "withholding": "Retenue",
        "net_received": "Net reçu",
        "total": "Total",
        "tax_impact": "**Impact fiscal**",
        "item": "Élément",
        "amount": "Montant",
        "other_annual_income": "Autres revenus annuels",
        "rrsp_withdrawal": "Retrait REER",
        "capital_gain_50": "Gain capital (50% de",
        "total_taxable_income": "Revenu imposable total",
        "federal_bpa": "MPA fédéral (non imposé)",
        "quebec_bpa": "MPA Québec (non imposé)",
        "dividend_tax_credit": "Crédit d'impôt dividendes",
        "tax_before_credits": "Impôt avant crédits",
        "tax_on_withdrawals_row": "Impôt sur retraits",
        "less_withholding": "Moins: Retenue payée",
        "owe_at_tax_time": "Dû à la déclaration",
        "marginal_rate_msg": "Votre taux marginal à",
        "income": "de revenu",
        "income_sources": "**Sources de revenus**",
        "optimization_tips": "Conseils d'optimisation",
        "tip_use_more_tfsa": "**Utilisez plus de CELI** — C'est libre d'impôt et n'affecte pas la PSV.",
        "tip_rrsp_triggered_clawback": "**Le REER a déclenché {} de récupération PSV** — Considérez utiliser le non enregistré ou le CELI.",
        "tip_non_reg_more_efficient": "**Le non enregistré est plus avantageux** — Taux effectif sur gains (~{}%) est inférieur au REER ({}%).",
        "tip_over_oas_threshold": "**Vous dépassez le seuil PSV de {}** — Chaque dollar additionnel coûte 15¢ en récupération.",
        "tip_looks_reasonable": "Votre répartition actuelle semble raisonnable!",
        "tax_reference": "Référence fiscale (2025)",
        "combined_rates": "### Taux marginaux combinés (Fédéral + Québec)",
        "target_type": "Type de cible",
        "total_annual_cash": "Liquidités annuelles totales",
        "additional_cash": "Liquidités additionnelles (en plus des autres revenus)",
        "withdrawal_needed": "Retrait nécessaire",
        "you_already_have": "Vous avez déjà {} des autres revenus",
        "rrsp_withholding_title": "### Retenue REER (Québec)",
        "up_to": "Jusqu'à",
        "over": "Plus de",
        "oas_clawback_title": "### Récupération PSV",
        "starts_at": "Début",
        "net_income": "de revenu net",
        "rate": "Taux",
        "of_income_over": "du revenu au-dessus du seuil",
        "max_oas": "PSV max (65-74)",
        "year": "an",
        "capital_gains_title": "### Gains en capital",
        "capital_gains_info": "Seulement 50% des gains sont imposables",
        "effective_max_rate": "Taux effectif max",
        "disclaimer": "Sources: TaxTips.ca, Canada.ca, Revenu Québec | À titre informatif seulement",
        "tax_on_other_income": "Impôt sur autres revenus",
        "total_annual_tax": "Impôt annuel total",
        "already_withheld": "Déjà retenu (paie)",
        "full_tax_picture": "**Portrait fiscal complet**",
        "net_annual_income": "Revenu annuel net",
        "gross_income": "Revenu brut (autres + retraits)",
        "less_total_tax": "Moins: Impôt total",
        "net_after_tax": "Net après impôt",
        "download_csv": "Télécharger résultats (CSV)",
        "download_filename": "resultats_impot_retraits.csv"
    }
}

# =============================================================================
# TAX DATA (2025)
# =============================================================================

FEDERAL_BRACKETS = [
    (57_375, 0.145),
    (114_750, 0.205),
    (177_882, 0.26),
    (253_414, 0.29),
    (float('inf'), 0.33)
]

QUEBEC_BRACKETS = [
    (53_255, 0.14),
    (106_495, 0.19),
    (129_590, 0.24),
    (float('inf'), 0.2575)
]

FEDERAL_BPA = 16_129
QUEBEC_BPA = 18_571
QUEBEC_ABATEMENT = 0.165

OAS_CLAWBACK_THRESHOLD = 93_454
OAS_MAX_ANNUAL = 8_820

CAPITAL_GAINS_INCLUSION = 0.50


# =============================================================================
# TAX CALCULATION FUNCTIONS
# =============================================================================

def calculate_bracket_tax(income: float, brackets: list) -> float:
    if income <= 0:
        return 0.0
    tax = 0.0
    prev_threshold = 0.0
    for threshold, rate in brackets:
        if income <= prev_threshold:
            break
        taxable = min(income, threshold) - prev_threshold
        if taxable > 0:
            tax += taxable * rate
        prev_threshold = threshold
    return tax


def get_marginal_rate(income: float, brackets: list) -> float:
    for threshold, rate in brackets:
        if income <= threshold:
            return rate
    return brackets[-1][1]


def calculate_quebec_tax(taxable_income: float, dividend_grossed_up: float = 0) -> tuple:
    """Calculate Quebec + Federal tax with dividend tax credit."""
    fed_gross = calculate_bracket_tax(taxable_income, FEDERAL_BRACKETS)
    fed_bpa_credit = FEDERAL_BPA * FEDERAL_BRACKETS[0][1] * (1 - QUEBEC_ABATEMENT)
    fed_after_abatement = fed_gross * (1 - QUEBEC_ABATEMENT)
    
    # Federal dividend tax credit: 15.0198% of grossed-up amount (eligible dividends)
    fed_div_credit = dividend_grossed_up * 0.150198 * (1 - QUEBEC_ABATEMENT)
    
    fed_net = max(0, fed_after_abatement - fed_bpa_credit - fed_div_credit)
    
    qc_gross = calculate_bracket_tax(taxable_income, QUEBEC_BRACKETS)
    qc_bpa_credit = QUEBEC_BPA * QUEBEC_BRACKETS[0][1]
    
    # Quebec dividend tax credit: 11.70% of grossed-up amount (eligible dividends)
    qc_div_credit = dividend_grossed_up * 0.117
    
    qc_net = max(0, qc_gross - qc_bpa_credit - qc_div_credit)
    
    # Return credits for display
    total_div_credit = fed_div_credit + qc_div_credit
    
    return fed_net, qc_net, fed_net + qc_net, total_div_credit


def calculate_incremental_tax(base_income: float, additional_income: float, base_div: float = 0, add_div: float = 0) -> float:
    """
    Calculate tax on additional income only.
    
    The BPA shelters the first ~$16k (fed) / ~$18k (QC) of TOTAL income.
    If base_income already exceeds BPA, the additional income is fully taxable.
    If base_income is below BPA, some of the additional income may be sheltered.
    """
    if additional_income <= 0:
        return 0.0
    
    total_income = base_income + additional_income
    total_div = base_div + add_div
    
    # Calculate total tax on all income, then subtract tax on base income
    # This properly handles the progressive brackets and BPA
    
    _, _, total_tax, _ = calculate_quebec_tax(total_income, total_div)
    _, _, base_tax, _ = calculate_quebec_tax(base_income, base_div)
    
    return total_tax - base_tax


def calculate_rrsp_withholding(amount: float) -> float:
    if amount <= 0:
        return 0.0
    if amount <= 5000:
        return amount * 0.19
    elif amount <= 15000:
        return amount * 0.24
    else:
        return amount * 0.29


def calculate_oas_clawback(net_income: float) -> tuple:
    if net_income <= OAS_CLAWBACK_THRESHOLD:
        return OAS_MAX_ANNUAL, 0.0, OAS_MAX_ANNUAL
    excess = net_income - OAS_CLAWBACK_THRESHOLD
    clawback = min(excess * 0.15, OAS_MAX_ANNUAL)
    return OAS_MAX_ANNUAL, clawback, OAS_MAX_ANNUAL - clawback


def get_combined_marginal_rate(income: float) -> float:
    fed_rate = get_marginal_rate(income, FEDERAL_BRACKETS) * (1 - QUEBEC_ABATEMENT)
    qc_rate = get_marginal_rate(income, QUEBEC_BRACKETS)
    return fed_rate + qc_rate


# =============================================================================
# STREAMLIT UI
# =============================================================================

st.set_page_config(
    page_title="Tax Calculator / Calculateur d'impôt",
    page_icon="💰",
    layout="wide"
)

# Language selector at top
lang_col1, lang_col2 = st.columns([6, 1])
with lang_col2:
    lang = st.selectbox("🌐", ["English", "Français"], label_visibility="collapsed")
    L = LANG["en"] if lang == "English" else LANG["fr"]

st.title(L["title"])
st.markdown(L["subtitle"])

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    st.header(L["your_situation"])
    
    age = st.number_input(L["your_age"], min_value=55, max_value=95, value=65)
    
    st.markdown("---")
    st.subheader(L["annual_income"])
    
    employment_income = st.number_input(
        L["employment_pension"],
        min_value=0,
        max_value=500_000,
        value=0,
        step=1_000,
        help=L["employment_pension_help"]
    )
    
    cpp_qpp_income = st.number_input(
        L["cpp_qpp"],
        min_value=0,
        max_value=30_000,
        value=0,
        step=100,
        help=L["cpp_qpp_help"],
        disabled=(age < 60)
    )
    
    oas_income = st.number_input(
        L["oas_psv"],
        min_value=0,
        max_value=15_000,
        value=0,
        step=100,
        help=L["oas_psv_help"],
        disabled=(age < 65)
    )
    
    dividend_income = st.number_input(
        L["dividends"],
        min_value=0,
        max_value=200_000,
        value=0,
        step=100,
        help=L["dividends_help"]
    )
    
    crypto_gains = st.number_input(
        L["crypto"],
        min_value=0,
        max_value=500_000,
        value=0,
        step=100,
        help=L["crypto_help"]
    )
    
    # Dividend gross-up (38% for eligible dividends)
    dividend_grossed_up = dividend_income * 1.38
    # Crypto is capital gain - 50% taxable
    crypto_taxable = crypto_gains * 0.50
    
    # Total other income (for cash flow: actual amounts received)
    other_income_cash = employment_income + cpp_qpp_income + oas_income + dividend_income + crypto_gains
    # Total taxable income from other sources
    other_income = employment_income + cpp_qpp_income + oas_income + dividend_grossed_up + crypto_taxable
    receives_oas = oas_income > 0
    
    st.markdown("---")
    st.subheader(L["account_balances"])
    
    rrsp_balance = st.number_input(
        L["rrsp_balance"],
        min_value=0,
        max_value=5_000_000,
        value=0,
        step=10_000
    )
    
    tfsa_balance = st.number_input(
        L["tfsa_balance"],
        min_value=0,
        max_value=500_000,
        value=0,
        step=5_000
    )
    
    non_reg_balance = st.number_input(
        L["non_reg_balance"],
        min_value=0,
        max_value=2_000_000,
        value=0,
        step=10_000
    )
    
    if non_reg_balance > 0:
        non_reg_acb = st.number_input(
            L["non_reg_acb"],
            min_value=0,
            max_value=non_reg_balance,
            value=int(non_reg_balance * 0.6),
            step=5_000,
            help=L["non_reg_acb_help"]
        )
        unrealized_gain = non_reg_balance - non_reg_acb
        gain_pct = (unrealized_gain / non_reg_balance * 100) if non_reg_balance > 0 else 0
        st.caption(f"{L['unrealized_gain']}: {unrealized_gain:,.0f} $ ({gain_pct:.0f}%)")
        gain_ratio = unrealized_gain / non_reg_balance if non_reg_balance > 0 else 0
    else:
        non_reg_acb = 0
        gain_ratio = 0

# =============================================================================
# MAIN - WITHDRAWAL SPLIT
# =============================================================================

st.markdown("---")
st.header(L["how_much_need"])

# Target type selection
target_col1, target_col2 = st.columns([1, 2])

with target_col1:
    target_options = [L["total_annual_cash"], L["additional_cash"]]
    target_type = st.radio(L["target_type"], target_options, index=0, horizontal=True)

with target_col2:
    cash_target = st.number_input(
        L["total_cash_needed"],
        min_value=0,
        max_value=500_000,
        value=0,
        step=1_000
    )

# Calculate actual withdrawal needed based on target type
# Note: other_income is gross, but we need to estimate net (after tax on paycheck)
_, _, tax_on_other, _ = calculate_quebec_tax(other_income, dividend_grossed_up)
other_income_net = other_income_cash - tax_on_other  # Approximate net after tax (use cash, not taxable)

if target_type == L["total_annual_cash"]:
    # User wants X total, already has other_income_net, so need to withdraw the difference
    withdrawal_target = max(0, cash_target - other_income_net)
    if other_income_net > 0:
        st.info(f"💡 {L['you_already_have'].format(f'{other_income_net:,.0f} $')} → {L['withdrawal_needed']}: **{withdrawal_target:,.0f} $**")
else:
    # User wants X additional on top of other income
    withdrawal_target = cash_target

st.markdown("---")
st.header(L["split_withdrawal"])
st.markdown(L["split_instructions"])

# Use withdrawal_target for defaults instead of cash_target
amount_needed = withdrawal_target

# Calculate smart defaults (TFSA first, then non-reg, then RRSP with withholding)
default_tfsa = min(tfsa_balance, amount_needed)
remaining_for_non_reg = max(0, amount_needed - default_tfsa)
default_non_reg = min(non_reg_balance, remaining_for_non_reg)
remaining_for_rrsp = max(0, remaining_for_non_reg - default_non_reg)

# For RRSP, gross up for withholding
if remaining_for_rrsp > 0 and rrsp_balance > 0:
    gross_needed = remaining_for_rrsp
    for _ in range(5):
        wh = calculate_rrsp_withholding(gross_needed)
        gross_needed = remaining_for_rrsp + wh
    default_rrsp = min(int(gross_needed), int(rrsp_balance))
else:
    default_rrsp = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(L["tfsa"])
    if tfsa_balance > 0:
        tfsa_withdrawal = st.number_input(
            L["from_tfsa"],
            min_value=0,
            max_value=int(tfsa_balance),
            value=int(default_tfsa),
            step=100,
            key="tfsa_input"
        )
    else:
        tfsa_withdrawal = 0
        st.number_input(L["from_tfsa"], min_value=0, max_value=1, value=0, disabled=True, key="tfsa_input")
    st.caption(f"{L['available']}: {tfsa_balance:,.0f} $")

with col2:
    st.subheader(L["non_reg"])
    if non_reg_balance > 0:
        non_reg_withdrawal = st.number_input(
            L["from_non_reg"],
            min_value=0,
            max_value=int(non_reg_balance),
            value=int(default_non_reg),
            step=100,
            key="non_reg_input"
        )
    else:
        non_reg_withdrawal = 0
        st.number_input(L["from_non_reg"], min_value=0, max_value=1, value=0, disabled=True, key="non_reg_input")
    st.caption(f"{L['available']}: {non_reg_balance:,.0f} $")

with col3:
    st.subheader(L["rrsp"])
    if rrsp_balance > 0:
        rrsp_withdrawal = st.number_input(
            L["from_rrsp"],
            min_value=0,
            max_value=int(rrsp_balance),
            value=int(default_rrsp),
            step=100,
            key="rrsp_input"
        )
    else:
        rrsp_withdrawal = 0
        st.number_input(L["from_rrsp"], min_value=0, max_value=1, value=0, disabled=True, key="rrsp_input")
    st.caption(f"{L['available']}: {rrsp_balance:,.0f} $")

# =============================================================================
# CALCULATE TAX IMPACT
# =============================================================================

rrsp_withholding = calculate_rrsp_withholding(rrsp_withdrawal)
rrsp_net = rrsp_withdrawal - rrsp_withholding

capital_gain = non_reg_withdrawal * gain_ratio if non_reg_withdrawal > 0 else 0
taxable_gain = capital_gain * CAPITAL_GAINS_INCLUSION

total_cash_received = tfsa_withdrawal + non_reg_withdrawal + rrsp_net

taxable_income_added = rrsp_withdrawal + taxable_gain
total_taxable_income = other_income + taxable_income_added

# Tax calculations with dividend tax credit
_, _, base_tax, base_div_credit = calculate_quebec_tax(other_income, dividend_grossed_up)  # Tax on other income alone
_, _, total_tax, total_div_credit = calculate_quebec_tax(total_taxable_income, dividend_grossed_up)  # Total tax on everything
incremental_tax = total_tax - base_tax  # Tax on withdrawals only

tax_at_filing = incremental_tax - rrsp_withholding

if receives_oas:
    _, base_clawback, _ = calculate_oas_clawback(other_income)
    _, new_clawback, _ = calculate_oas_clawback(total_taxable_income)
    oas_impact = new_clawback - base_clawback
else:
    oas_impact = 0

total_cost = incremental_tax + oas_impact

shortfall = amount_needed - total_cash_received

# =============================================================================
# RESULTS
# =============================================================================

st.markdown("---")
st.header(L["results"])

if shortfall > 0:
    st.error(f"{L['shortfall']}: {shortfall:,.0f} $ — {L['shortfall_msg']}")
elif shortfall < -100:
    st.warning(f"{L['surplus']}: {-shortfall:,.0f} $ — {L['surplus_msg']}")
else:
    st.success(f"{L['target_met']}: {total_cash_received:,.0f} $")

res_col1, res_col2, res_col3, res_col4 = st.columns(4)

with res_col1:
    st.metric(L["cash_received"], f"{total_cash_received:,.0f} $", 
              delta=f"{L['target']}: {amount_needed:,.0f} $", delta_color="off")

with res_col2:
    st.metric(L["tax_on_withdrawals"], f"{incremental_tax:,.0f} $")

with res_col3:
    st.metric(L["oas_clawback"], f"{oas_impact:,.0f} $" if receives_oas else L["na"])

with res_col4:
    effective_rate = (total_cost / total_cash_received * 100) if total_cash_received > 0 else 0
    st.metric(L["total_cost"], f"{total_cost:,.0f} $", 
              delta=f"{effective_rate:.1f}% {L['effective']}", delta_color="off")

# Breakdown
st.markdown("---")
st.subheader(L["breakdown"])

breakdown_col1, breakdown_col2, breakdown_col3 = st.columns(3)

tfsa_label = "CELI" if lang == "Français" else "TFSA"
non_reg_label = "Non enreg." if lang == "Français" else "Non-Reg"
rrsp_label = "REER" if lang == "Français" else "RRSP"
emp_label = "Emploi/Pension" if lang == "Français" else "Employment/Pension"
rrq_label = "RRQ/RPC" if lang == "Français" else "CPP/QPP"
psv_label = "PSV/SV" if lang == "Français" else "OAS/PSV"
div_label = "Dividendes" if lang == "Français" else "Dividends"
crypto_label = "Crypto" if lang == "Français" else "Crypto"

with breakdown_col1:
    st.markdown(L["income_sources"])
    st.markdown(f"""
    | Source | {L['amount']} |
    |--------|---------|
    | {emp_label} | {employment_income:,.0f} $ |
    | {rrq_label} | {cpp_qpp_income:,.0f} $ |
    | {psv_label} | {oas_income:,.0f} $ |
    | {div_label} | {dividend_income:,.0f} $ |
    | {crypto_label} | {crypto_gains:,.0f} $ |
    | **Total** | **{other_income_cash:,.0f} $** |
    """)
    
    st.markdown(L["withdrawals"])
    st.markdown(f"""
    | {L['account']} | {L['net_received']} |
    |---------|--------------|
    | {tfsa_label} | {tfsa_withdrawal:,.0f} $ |
    | {non_reg_label} | {non_reg_withdrawal:,.0f} $ |
    | {rrsp_label} | {rrsp_net:,.0f} $ |
    | **Total** | **{total_cash_received:,.0f} $** |
    """)

with breakdown_col2:
    st.markdown(L["tax_impact"])
    
    # Show dividend credit if applicable
    div_credit_row = f"| {L['dividend_tax_credit']} | -{total_div_credit:,.0f} $ |" if dividend_income > 0 else ""
    
    st.markdown(f"""
    | {L['item']} | {L['amount']} |
    |---------|---------|
    | {emp_label} | {employment_income:,.0f} $ |
    | {rrq_label} | {cpp_qpp_income:,.0f} $ |
    | {psv_label} | {oas_income:,.0f} $ |
    | {div_label} (×1.38) | {dividend_grossed_up:,.0f} $ |
    | {crypto_label} (50%) | {crypto_taxable:,.0f} $ |
    | + {L['rrsp_withdrawal']} | {rrsp_withdrawal:,.0f} $ |
    | + {L['capital_gain_50']} {capital_gain:,.0f} $) | {taxable_gain:,.0f} $ |
    | **{L['total_taxable_income']}** | **{total_taxable_income:,.0f} $** |
    """)

with breakdown_col3:
    st.markdown("**Calcul impôt**" if lang == "Français" else "**Tax Calculation**")
    
    st.markdown(f"""
    | {L['item']} | {L['amount']} |
    |---------|---------|
    | {L['federal_bpa']} | -{FEDERAL_BPA:,.0f} $ |
    | {L['quebec_bpa']} | -{QUEBEC_BPA:,.0f} $ |
    | {L['dividend_tax_credit']} | -{total_div_credit:,.0f} $ |
    | | |
    | {L['tax_on_other_income']} | {base_tax:,.0f} $ |
    | {L['tax_on_withdrawals_row']} | {incremental_tax:,.0f} $ |
    | **{L['total_annual_tax']}** | **{total_tax:,.0f} $** |
    | | |
    | {L['already_withheld']} | ~{base_tax:,.0f} $ |
    | {L['less_withholding']} | -{rrsp_withholding:,.0f} $ |
    | **{L['owe_at_tax_time']}** | **{tax_at_filing:,.0f} $** |
    """)

# Net Annual Income Summary
st.markdown("---")
st.subheader(L["net_annual_income"])

# Calculate total gross (cash received) and net
# other_income_cash is the actual cash received (not grossed-up dividends)
gross_total = other_income_cash + total_cash_received
net_annual = gross_total - total_tax

net_col1, net_col2, net_col3 = st.columns(3)

with net_col1:
    st.metric(L["gross_income"], f"{gross_total:,.0f} $")

with net_col2:
    st.metric(L["less_total_tax"], f"-{total_tax:,.0f} $")

with net_col3:
    st.metric(L["net_after_tax"], f"{net_annual:,.0f} $")

# Calculate marginal rate (needed for CSV and display)
marginal_rate = get_combined_marginal_rate(total_taxable_income)

# CSV Download
import io
csv_data = io.StringIO()

if lang == "Français":
    csv_data.write("Catégorie,Élément,Montant\n")
    csv_data.write(f"Revenus,Emploi/Pension,{employment_income}\n")
    csv_data.write(f"Revenus,RRQ/RPC,{cpp_qpp_income}\n")
    csv_data.write(f"Revenus,PSV/SV,{oas_income}\n")
    csv_data.write(f"Revenus,Dividendes,{dividend_income}\n")
    csv_data.write(f"Revenus,Dividendes majorés (38%),{dividend_grossed_up:.0f}\n")
    csv_data.write(f"Revenus,Crypto/Actifs numériques,{crypto_gains}\n")
    csv_data.write(f"Revenus,Crypto imposable (50%),{crypto_taxable:.0f}\n")
    csv_data.write(f"Revenus,Total revenus (imposable),{other_income:.0f}\n")
    csv_data.write(f"Retraits,CELI,{tfsa_withdrawal}\n")
    csv_data.write(f"Retraits,Non enregistré,{non_reg_withdrawal}\n")
    csv_data.write(f"Retraits,REER (brut),{rrsp_withdrawal}\n")
    csv_data.write(f"Retraits,Retenue REER,{rrsp_withholding}\n")
    csv_data.write(f"Retraits,REER (net),{rrsp_net}\n")
    csv_data.write(f"Retraits,Total reçu,{total_cash_received}\n")
    csv_data.write(f"Gains capital,Gain réalisé (non-enreg),{capital_gain}\n")
    csv_data.write(f"Gains capital,Gain imposable (50%),{taxable_gain}\n")
    csv_data.write(f"Impôts,Revenu imposable total,{total_taxable_income}\n")
    csv_data.write(f"Impôts,Impôt sur autres revenus,{base_tax}\n")
    csv_data.write(f"Impôts,Impôt sur retraits,{incremental_tax}\n")
    csv_data.write(f"Impôts,Impôt annuel total,{total_tax}\n")
    csv_data.write(f"Impôts,Récupération PSV,{oas_impact}\n")
    csv_data.write(f"Impôts,Dû à la déclaration,{tax_at_filing}\n")
    csv_data.write(f"Sommaire,Revenu brut total (cash),{gross_total}\n")
    csv_data.write(f"Sommaire,Impôt total,{total_tax}\n")
    csv_data.write(f"Sommaire,Revenu net après impôt,{net_annual}\n")
    csv_data.write(f"Sommaire,Taux marginal,{marginal_rate*100:.1f}%\n")
else:
    csv_data.write("Category,Item,Amount\n")
    csv_data.write(f"Income,Employment/Pension,{employment_income}\n")
    csv_data.write(f"Income,CPP/QPP,{cpp_qpp_income}\n")
    csv_data.write(f"Income,OAS/PSV,{oas_income}\n")
    csv_data.write(f"Income,Dividends,{dividend_income}\n")
    csv_data.write(f"Income,Dividends grossed-up (38%),{dividend_grossed_up:.0f}\n")
    csv_data.write(f"Income,Crypto/Digital Assets,{crypto_gains}\n")
    csv_data.write(f"Income,Crypto taxable (50%),{crypto_taxable:.0f}\n")
    csv_data.write(f"Income,Total income (taxable),{other_income:.0f}\n")
    csv_data.write(f"Withdrawals,TFSA,{tfsa_withdrawal}\n")
    csv_data.write(f"Withdrawals,Non-Registered,{non_reg_withdrawal}\n")
    csv_data.write(f"Withdrawals,RRSP (gross),{rrsp_withdrawal}\n")
    csv_data.write(f"Withdrawals,RRSP withholding,{rrsp_withholding}\n")
    csv_data.write(f"Withdrawals,RRSP (net),{rrsp_net}\n")
    csv_data.write(f"Withdrawals,Total received,{total_cash_received}\n")
    csv_data.write(f"Capital Gains,Realized gain (non-reg),{capital_gain}\n")
    csv_data.write(f"Capital Gains,Taxable gain (50%),{taxable_gain}\n")
    csv_data.write(f"Taxes,Total taxable income,{total_taxable_income}\n")
    csv_data.write(f"Taxes,Tax on other income,{base_tax}\n")
    csv_data.write(f"Taxes,Tax on withdrawals,{incremental_tax}\n")
    csv_data.write(f"Taxes,Total annual tax,{total_tax}\n")
    csv_data.write(f"Taxes,OAS clawback,{oas_impact}\n")
    csv_data.write(f"Taxes,Owe at tax time,{tax_at_filing}\n")
    csv_data.write(f"Summary,Total gross income (cash),{gross_total}\n")
    csv_data.write(f"Summary,Total tax,{total_tax}\n")
    csv_data.write(f"Summary,Net income after tax,{net_annual}\n")
    csv_data.write(f"Summary,Marginal rate,{marginal_rate*100:.1f}%\n")

st.download_button(
    label=L["download_csv"],
    data=csv_data.getvalue(),
    file_name=L["download_filename"],
    mime="text/csv"
)

# Marginal rate display
st.markdown("---")
st.info(f"{L['marginal_rate_msg']} {total_taxable_income:,.0f} $ {L['income']}: **{marginal_rate*100:.1f}%**")

# =============================================================================
# OPTIMIZATION TIPS
# =============================================================================

st.markdown("---")
with st.expander(L["optimization_tips"]):
    tips = []
    
    if tfsa_withdrawal < tfsa_balance and tfsa_withdrawal < amount_needed:
        tips.append(L["tip_use_more_tfsa"])
    
    if rrsp_withdrawal > 0 and receives_oas and oas_impact > 0:
        tips.append(L["tip_rrsp_triggered_clawback"].format(f"{oas_impact:,.0f} $"))
    
    if rrsp_withdrawal > 0 and non_reg_balance > 0 and non_reg_withdrawal < non_reg_balance:
        rrsp_tax_rate = incremental_tax / rrsp_withdrawal if rrsp_withdrawal > 0 else 0
        non_reg_effective = gain_ratio * CAPITAL_GAINS_INCLUSION * marginal_rate
        if rrsp_tax_rate > non_reg_effective:
            tips.append(L["tip_non_reg_more_efficient"].format(f"{non_reg_effective*100:.0f}", f"{rrsp_tax_rate*100:.0f}"))
    
    if total_taxable_income > OAS_CLAWBACK_THRESHOLD and receives_oas:
        over_threshold = total_taxable_income - OAS_CLAWBACK_THRESHOLD
        tips.append(L["tip_over_oas_threshold"].format(f"{over_threshold:,.0f} $"))
    
    if not tips:
        tips.append(L["tip_looks_reasonable"])
    
    for tip in tips:
        st.markdown(f"- {tip}")

# =============================================================================
# REFERENCE
# =============================================================================

with st.expander(L["tax_reference"]):
    st.markdown(f"""
    {L['combined_rates']}
    | {L['income']} | {L['rate']} |
    |--------|------|
    | 0 $ - 53 255 $ | 26,11% |
    | 53 255 $ - 57 375 $ | 31,11% |
    | 57 375 $ - 106 495 $ | 36,12% |
    | 106 495 $ - 114 750 $ | 41,12% |
    | 114 750 $ - 129 590 $ | 45,71% |
    | 129 590 $ - 177 882 $ | 47,46% |
    | 177 882 $ - 253 414 $ | 49,96% |
    | > 253 414 $ | 53,31% |
    
    {L['rrsp_withholding_title']}
    | {L['amount']} | {L['rate']} |
    |---------|------|
    | {L['up_to']} 5 000 $ | 19% |
    | 5 001 $ - 15 000 $ | 24% |
    | {L['over']} 15 000 $ | 29% |
    
    {L['oas_clawback_title']}
    - {L['starts_at']}: 93 454 $ {L['net_income']}
    - {L['rate']}: 15% {L['of_income_over']}
    - {L['max_oas']}: 8 820 $/{L['year']}
    
    {L['capital_gains_title']}
    - {L['capital_gains_info']}
    - {L['effective_max_rate']}: ~26,65%
    """)

st.markdown("---")
st.caption(L["disclaimer"])
