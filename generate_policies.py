# BANNED MODIFIERS: dev cost, core cost, diplo annex cost, admin eff, anything related to gov cap, province warscore cost, innovativeness gain, idea cost, tech cost
# players shouldnt be "forced" to take a specific 2-idea combo if their playstyle revolves around these modifiers
# or to turn on/off policies as they tech up/take ideas

# format: (adm, dip, mil, adm, dip, mil) 0-indexed

# for each pair of ideas:
#   select a category (adm, dip, or mil)
#   if adm: select adm modifier [0 or 3] from among the pair, then select another adm or dip modifier [0, 1, 3, 4] from among the unchosen in the pair
#   if dip: select dip modifier [1 or 4] from among the pair, then select another adm or dip modifier [0, 1, 3, 4] from among the unchosen in the pair
#   if mil: select mil modifier [2 or 5] from among the pair, then select an adm or dip modifier [0, 1, 3, 4] from the pair randomly

# in practice, this means mil policies will get exactly 1 military modifier, and nothing else will have any mil modifiers
# and each policy will have a modifier from their category, and another from either their category or adm/dip

adm = {
    "innovativeness_ideas": ("advisor_cost = -0.1", "trade_efficiency = 0.1", "infantry_power = 0.075", "global_institution_spread = 0.25", "reform_progress_growth = 0.15", "artillery_power = 0.075"),
    "religious_ideas": ("missionary_strength = 0.015", "tolerance_own = 1", "morale_damage = 0.075", "max_absolutism = 5", "reverse_relation_with_same_religion = 10", "fire_damage_received = -0.075"),
    "economic_ideas": ("inflation_reduction = 0.1", "build_time = -0.1", "land_forcelimit_modifier = 0.15", "global_tax_modifier = 0.15", "heavy_ship_power = 0.1", "drill_decay_modifier = -0.25"),
    "expansion_ideas": ("build_cost = -0.1", "global_colonial_growth = 10" , "global_manpower_modifier = 0.15", "religious_unity = 0.1", "trade_steering = 0.25", "merc_leader_army_tradition = 0.25"), # todo
    "administrative_ideas": ("overextension_impact_modifier = -0.05", "adm_advisor_cost = -0.2", "yearly_army_professionalism = 0.002", "global_autonomy = -0.075", "yearly_corruption = -0.1", "mercenary_discipline = 0.05"),
    "humanist_ideas": ("global_unrest  = -1", "improve_relations = 0.15", "land_leader_maneuver = 1", "stability_cost_modifier = -0.15", "merchants = 1", "morale_damage_received = -0.075"),
    "infrastructure_ideas": ("build_time = -0.1", "global_trade_power = 0.1", "movement_speed = 0.075", "interest = -0.05", "envoy_travel_time = -0.33", "reinforce_speed = 0.15"),
    "extraction_ideas": ("global_trade_goods_size_modifier = 0.075",  "production_efficiency = 0.1", "mercenary_cost = -0.15", "loot_amount = 0.5", "vassal_income = 0.25", "siege_ability = 0.15"),
    "urbanization_ideas": ("global_prosperity_growth = 0.25", "num_accepted_cultures = 1", "mercenary_manpower = 0.25", "global_autonomy = -0.075", "estate_interaction_cooldown_modifier = -0.20", "land_leader_fire = 1"),
    "militarist_ideas": ("war_exhaustion = -0.03", "reinforce_cost_modifier = -0.15", "leader_cost = -0.15", "global_unrest = -1", "mil_advisor_cost = -0.2", "army_tradition_decay = -0.01"),
    "federalist_ideas": ("state_maintenance_modifier = -0.25", "diplomatic_reputation = 1", "discipline = 0.035", "state_maintenance_modifier = -0.25", "reduced_liberty_desire_on_same_continent = 10", "attack_bonus_in_capital_terrain = 1"),
    "governance_ideas": ("global_tax_modifier = 0.15", "global_own_trade_power = 0.1", "reserves_organisation = 0.1", "years_of_nationalism = -5", "diplomatic_upkeep = 1", "reinforce_speed = 0.15"),
    "metallurgy_ideas": ("prestige = 1", "caravan_power = 0.25", "fire_damage = 0.075", "monthly_gold_inflation_modifier = -0.25", "global_prov_trade_power_modifier = 0.1", "infantry_fire = 0.1")
}
dip = {
    "spy_ideas": ("max_absolutism = 5", "siege_blockade_progress = 1", "artillery_levels_available_vs_fort = 1", "interest = -0.05", "diplomats = 1", "harsh_treatment_cost = -0.25")
}
mil = {
    
}