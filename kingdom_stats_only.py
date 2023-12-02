import random

# Leadership Roles
Ruler = 0.1  # Bloodfist
Consort = 0  # None
Councilor = 4  # Elion Greenwhisper
General = 0  # None
GrandDiplomat = 0  # None
Heir = 0  # None
HighPriest = 3  # Draexyz
Magister = 0  # None
Marshal = 0  # None
RoyalEnforcer = 5  # Rena
Spymaster = 0  # None
Treasurer = 3  # Phoibe
Viceroy = 0  # None
Warden = 0  # None
Alignment = 4  # Chaotic Good; +4 Loyalty

# Kingdom Statistics
Loyalty = Consort/2 + Councilor + Heir + RoyalEnforcer + Warden
Size = 1
Stability = General + GrandDiplomat + HighPriest
Treasury = 0
Unrest = 0
Economy = Magister + Marshal + Treasurer + Viceroy/2
BuildPoints = 23
Defense = 0
Consumption = 0
Districts = 2
Misc = 0
ControlDC = Size + Districts + Misc
Taxes = True
ConsortIsRuler = False

# Check for Penalties
if Ruler == 0:
    print("A kingdom without a ruler cannot claim new hexes, create Farms, build Roads, or purchase settlement districts. Unrest increases by 4 during the kingdom’s Upkeep Phase.")
    Unrest += 4
    if Consort < 0:
        Unrest += 4
        print("If the ruler is unavailable during a turn, you may act as the Ruler for that turn, negating the vacancy penalty for having no Ruler, though you do not gain the Ruler benefit.")
        ConsortIsRuler = True

if Councilor == 0:
    Loyalty -= 2
    print("Councilor is unavailable: The kingdom gains no benefits from the Holiday edict. During the Upkeep Phase, Unrest increases by 1.")
    HolidayEdict = False

if General == 0:
    Loyalty -= 4

if GrandDiplomat == 0:
    Stability -= 2
    print("Grand diplomat is unavailable: You can't issue diplomatic and exploration edicts.")
    DiplomaticEdicts = False
    ExplorationEdicts = False

# No penalty for Heir
if HighPriest == 0:
    Stability -= 2
    Unrest += 1

if Magister == 0:
    Economy -= 4

if Marshal == 0:
    Economy -= 4

# No Penalty for Royal Enforcer
if Spymaster == 0:
    Economy -= 4
    Unrest += 1

if Treasurer == 0:
    Economy += 0  # Seems redundant; consider removing
    print("Treasurer unavailable. During the Edict Phase, when you would normally collect taxes, the kingdom does not collect taxes at all and the taxation level is considered 'none'.")
    Taxes = False

if Viceroy == 0:
    VassalRuler = False

if Warden == 0:
    Loyalty -= 2
    Stability -= 2

# Districts
def Fort():
    global Stability, Defense, Consumption
    Stability += 2
    Defense += 4
    Consumption += 1
    Stable()
    Barracks()

def Barracks():
    global Defense
    Defense += 2

def Stable():
    global Economy, Stability
    Economy += 1
    Stability -= 1

Fort()

print(f"Your loyalty is: {Loyalty}")
print(f"Your size is: {Size}")
print(f"Your treasury is: {Treasury}")
print(f"Your unrest is: {Unrest}")
print(f"Your Economy is: {Economy}")
print(f"You have {BuildPoints} Build Points")
print(f"Your defense is: {Defense}")
print(f"Your consumption is: {Consumption}")
print(f"You have {Districts} districts")
print(f"Your control DC is at: {ControlDC}")
