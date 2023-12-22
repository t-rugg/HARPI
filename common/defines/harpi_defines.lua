-- Format for overwriting define values:
--
-- NDefines.NDiplomacy.MAX_CLIENT_STATES = 20

-- HARPI values
NDefines.NCountry.MAX_IDEA_GROUPS_FROM_SAME_CATEGORY = 0.35 -- from 1-1-0 to 1-1-1
NDefines.NCountry.FREE_IDEA_GROUP_COST  = 4	-- from 3
NDefines.NCountry.IDEA_TO_TECH = -0.01	-- from -2%. twice as many groups means we halve the tech cost reduction
                                        -- this is probably a safe assumption since the reduction is only really significant lategame
NDefines.NCountry.PS_BUY_IDEA = 300 -- from 400. idea groups are meant to be about ~75% as powerful as a "strong group" in vanilla, give or take
NDefines.NCountry.INNOVATIVENESS_FIRST_PICKED_IDEA = 0.5 -- from 2 (low because there are more idea groups, i.e. much easier to get a unique one)

-- vanilla values that may be useful to change later
NDefines.NCountry.MAX_ACTIVE_POLICIES = 5
NDefines.NCountry.BASE_POSSIBLE_POLICIES = 3
NDefines.NCountry.BASE_FREE_POLICIES = 1
NDefines.NCountry.ABANDON_IDEAGROUP_REFUND = 0.10 -- might want to lower this? potentially abusable
                                                  -- tbh I'm not even sure why this is a mechanic, I might just make it 0