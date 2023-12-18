# BANNED MODIFIERS: dev cost, core cost, diplo annex cost, admin eff, anything related to gov cap, province warscore cost, innovativeness gain, idea cost, tech cost, accept vassal reasons, num/cost accepted cultures
# players shouldnt be "forced" to take a specific 2-idea combo if their playstyle revolves around these modifiers
# or to turn on/off policies as they tech up/take ideas
#
# anything related to dice rolls (e.g. own terrain bonus) or artillery levels in siege is also banned due to being too stackable EXCEPT for leader pips (because those have a natural cap)
# diplomats, missionaries, merchants, colonists are banned for similar reasons
#
# bans do not apply to legalist ideas policies, but only ONE policy can have a given banned modifier (so urbanization and infrastructure can't both have dev cost for example)

# format: (adm, dip, mil, adm, dip, mil) 0-indexed

# for each pair of ideas:
#   select a category (adm, dip, or mil)
#   if adm: select adm modifier [0 or 3] from among the pair, then select another adm or dip modifier [0, 1, 3, 4] from among the unchosen in the pair
#   if dip: select dip modifier [1 or 4] from among the pair, then select another adm or dip modifier [0, 1, 3, 4] from among the unchosen in the pair
#   if mil: select mil modifier [2 or 5] from among the pair, then select an adm or dip modifier [0, 1, 3, 4] from the pair randomly
#
# in practice, this means mil policies will get exactly 1 military modifier, and nothing else will have any mil modifiers
# and each policy will have a modifier from their category, and another from adm/dip

# TODO: legacies? decide what to do with these. I think I'll just not give them any policies (legacies are already strong, no policies is a legitimate downside) but that seems really unfun

import random
random.seed("HARPI")

adm = {
	"innovativeness_ideas": ("advisor_cost = -0.1", "trade_efficiency = 0.1", "infantry_power = 0.075", "global_institution_spread = 0.25", "reform_progress_growth = 0.15", "artillery_fire = 0.02"),
	"religious_ideas": ("missionary_strength = 0.015", "tolerance_own = 1.5", "morale_damage = 0.075", "max_absolutism = 5", "reverse_relation_with_same_religion = 10", "fire_damage_received = -0.075"),
	"economic_ideas": ("inflation_reduction = 0.1", "build_time = -0.1", "land_forcelimit_modifier = 0.15", "global_tax_modifier = 0.15", "heavy_ship_power = 0.1", "drill_decay_modifier = -0.25"),
	"expansion_ideas": ("build_cost = -0.1", "global_colonial_growth = 10" , "global_manpower_modifier = 0.15", "religious_unity = 0.1", "trade_steering = 0.25", "merc_leader_army_tradition = 0.25"), # todo
	"administrative_ideas": ("overextension_impact_modifier = -0.05", "adm_advisor_cost = -0.2", "yearly_army_professionalism = 0.002", "global_autonomy = -0.075", "yearly_corruption = -0.1", "mercenary_discipline = 0.05"),
	"humanist_ideas": ("global_unrest  = -1", "improve_relations = 0.15", "land_leader_maneuver = 1", "stability_cost_modifier = -0.15", "global_sailors_modifier = 0.2", "morale_damage_received = -0.075"),
	"infrastructure_ideas": ("build_time = -0.1", "global_trade_power = 0.1", "movement_speed = 0.075", "interest = -0.5", "envoy_travel_time = -0.33", "reinforce_speed = 0.15"),
	"extraction_ideas": ("global_trade_goods_size_modifier = 0.075",  "production_efficiency = 0.1", "mercenary_cost = -0.15", "loot_amount = 0.5", "vassal_income = 0.25", "siege_ability = 0.15"),
	"urbanization_ideas": ("global_prosperity_growth = 0.25", "naval_forcelimit_modifier = 0.15", "mercenary_manpower = 0.25", "global_autonomy = -0.075", "estate_interaction_cooldown_modifier = -0.20", "land_leader_fire = 1"),
	"militarist_ideas": ("war_exhaustion = -0.03", "reinforce_cost_modifier = -0.15", "leader_cost = -0.15", "global_unrest = -1", "mil_advisor_cost = -0.2", "army_tradition_decay = -0.01"),
	"federalist_ideas": ("state_maintenance_modifier = -0.25", "diplomatic_reputation = 1", "discipline = 0.035", "state_maintenance_modifier = -0.25", "reduced_liberty_desire_on_same_continent = 10", "defensiveness = 0.15"),
	"governance_ideas": ("global_tax_modifier = 0.15", "global_own_trade_power = 0.15", "reserves_organisation = 0.1", "years_of_nationalism = -5", "diplomatic_upkeep = 1", "reinforce_speed = 0.15"),
	"metallurgy_ideas": ("prestige = 1", "caravan_power = 0.25", "fire_damage = 0.075", "monthly_gold_inflation_modifier = -0.25", "global_prov_trade_power_modifier = 0.15", "infantry_fire = 0.1"),
	"parliamentary_ideas": ("all_estate_loyalty_equilibrium = 0.03", "diplomatic_reputation = 1", "manpower_recovery_speed = 0.15", "advisor_pool = 2", "trade_company_investment_cost = -0.1", "backrow_artillery_damage = 0.075")
}
dip = {
	"spy_ideas": ("max_absolutism = 5", "dip_advisor_cost = -0.2", "leader_siege = 1", "interest = -0.5", "global_foreign_trade_power = 0.15", "harsh_treatment_cost = -0.25"),
	"diplomatic_ideas": ("prestige = 1", "diplomatic_upkeep = 1", "yearly_army_professionalism = 0.002", "tolerance_heathen = 1.5", "reduced_trade_penalty_on_non_main_tradenode = 0.25", "manpower_in_accepted_culture_provinces = 0.2"),
	"trade_ideas": ("global_institution_spread = 0.25", "trade_company_investment_cost = -0.1", "discipline = 0.035", "reform_progress_growth = 0.15", "leader_naval_manuever = 1", "mercenary_discipline = 0.05"),
	"exploration_ideas": (),
	"maritime_ideas": (),
	"court_ideas": (),
	"influence_ideas": (),
	"stewardship_ideas": (),
	"patronage_ideas": (),
	# legalist ideas get special handling
	"realist_ideas": (),
	"integration_ideas": (),
	"authority_ideas": (),
	"imperialist_ideas": (),
	"adventure_ideas": (),
	"monastic_ideas": (),
	"lawful_ideas": (),
	"chaotic_ideas": (),
}
mil = {
	"offensive_ideas": ("loot_amount = 0.5", "heavy_ship_cost = -0.1", "shock_damage = 0.075", "years_of_nationalism = -5", "trade_company_investment_cost = -0.1", "artillery_barrage_cost = -0.25"),
	"defensive_ideas": ("build_time = -0.1", "improve_relations = 0.15", "shock_damage_received = -0.075", "global_prosperity_growth = 0.25", "disengagement_chance = 0.1", "manpower_in_own_culture_provinces = 0.2")
}

combined = adm | dip | mil

# remove empty — allows for partial testing
ideas = {}
for entry in combined:
	if combined[entry] != ():
		ideas[entry] = combined[entry]

def getCategory(group):
	if group in adm:
		return "ADM"
	elif group in dip:
		return "DIP"
	elif group in mil:
		return "MIL"
	assert False, "failed to get category"

# the offset of each category in the modifier list of each idea group
categoryInt = {
	"ADM": 0,
	"DIP": 1, 
	"MIL": 2
}

# need to be tabs, not spaces!
formatter = '''{0}_{1}_policy = {{
	monarch_power = {2}

	potential = {{
		has_idea_group = {0}
		has_idea_group = {1}
	}}

	allow = {{
		full_idea_group = {0}
		full_idea_group = {1}
	}}
	
	{3}
	{4}
	
	effect = {{}}
	removed_effect = {{}}
	
	ai_will_do = {{
		factor = {5}
	}}
}}

'''

blacklist = []


# WARNING: this might be the worst code i have ever written
# be warned, ye who enter here
with open("generated_policies.txt", "w", encoding="windows-1252") as f: 
	# loop over pairs of idea groups from distinct categories
	for group1 in ideas:
		cat1 = getCategory(group1)
		blacklist.append(group1)
		for group2 in ideas:
			if group2 in blacklist:
				continue
			cat2 = getCategory(group2)
			if (cat1 != cat2):
				# get a random modifier from the appropriate category
				mainGroup = random.choice((group1, group2))
				cat = random.choice((cat1, cat2))
				mainMod = ideas[mainGroup][random.choice([0 + categoryInt[cat], 3 + categoryInt[cat]])] # I'M SORRY

				# get a random modifier from adm or dip modifiers of one of the groups
				# 2/3s chance to be subGroup, 1/3 to be MainGroup
				subGroup = random.choice((group1, group2, (group1 if group2 == mainGroup else group2)))
				# ensure subMod is different from mainMod
				subMod = mainMod # more like subMod = HARPI amirite????????
				while subMod == mainMod:
					subMod = ideas[subGroup][random.choice([0, 1, 3, 4])]

				formatted = formatter.format(group1, group2, cat, mainMod, subMod, "0.6")
				print(formatted, file=f)


###
### LEGALIST IDEAS
### 
				
legalist_adm = {
	"innovativeness_ideas": "technology_cost = -0.1",
	"religious_ideas": "missionaries = 1",
	"economic_ideas": "interest = -1.5",
	"expansion_ideas": "territories_governing_cost = -0.15",
	"administrative_ideas": "core_creation = -0.15",
	"humanist_ideas": "idea_cost = -0.1",
	"infrastructure_ideas": "",
	"extraction_ideas": "",
	"urbanization_ideas": "",
	"militarist_ideas": "",
	"federalist_ideas": "",
	"governance_ideas": "",
	"metallurgy_ideas": "",
	"parliamentary_ideas": "",
}
legalist_dip = {
	"filler": "",
}
legalist_mil = {
	"filler": "",
}

with open("generated_policies_legalist.txt", "w", encoding="windows-1252") as f:
	for group in legalist_adm:
		formatted = formatter.format(group, "legalist_ideas", "ADM", legalist_adm[group], "reform_progress_growth = 0.05", "1.2")
		print(formatted, file=f)
	for group in legalist_dip:
		formatted = formatter.format(group, "legalist_ideas", "DIP", legalist_dip[group], "reform_progress_growth = 0.05", "1.2")
		print(formatted, file=f)
	for group in legalist_mil:
		formatted = formatter.format(group, "legalist_ideas", "MIL", legalist_mil[group], "reform_progress_growth = 0.05", "1.2")
		print(formatted, file=f)