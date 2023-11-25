-- Format for overwriting define values:
--
-- NDefines.NDiplomacy.MAX_CLIENT_STATES = 20

-- HARPI values
NDefines.NCountry.MAX_IDEA_GROUPS_FROM_SAME_CATEGORY = 0.35 -- from 1-1-0 to 1-1-1
NDefines.NCountry.FREE_IDEA_GROUP_COST  = 4	-- from 3
NDefines.NCountry.IDEA_TO_TECH = -0.01	-- from -2%
NDefines.NCountry.PS_BUY_IDEA = 300 -- from 400. idea groups are meant to be about ~75% as powerful as a "strong group" in vanilla, give or take
NDefines.NCountry.INNOVATIVENESS_FIRST_PICKED_IDEA = 0.5 -- from 2

-- TEMPORARILY CHANGED FOR TESTING
NDefines.NCountry.MAX_ACTIVE_POLICIES = 0 -- from 5
NDefines.NCountry.BASE_POSSIBLE_POLICIES = 0 -- from 3

-- vanilla values that may be useful to change later
NDefines.NCountry.ABANDON_IDEAGROUP_REFUND = 0.10