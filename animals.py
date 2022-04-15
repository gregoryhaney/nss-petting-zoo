from asp import Asp
from bass import Bass
from cobra import Cobra
from cow import Cow
from gazelle import Gazelle
from guppy import Guppy
from koi import Koi
from leech import Leech
from moose import Moose
from oscar import Oscar
from reindeer import Reindeer
from salmon import Salmon
from slug import Slug
from wildebeast import Wildebeast
from worm import Worm




Edwin = Worm()
Edwin.name = "Edwin"
Edwin.species = "Earthworm"
Edwin.date_added = "20211009"

Silva = Slug()
Silva.name = "Silva"
Silva.species = "Humpback Slug"
Silva.date_added = "20220303"

Karen = Cobra()
Karen.name = "Karen"
Karen.species = "Kalifornia King"
Karen.date_added = "20190601"

Alice = Asp()
Alice.name = "Alice"
Alice.species = "American Asian"
Alice.date_added = "20160714"

Leo = Leech()
Leo.name = "Leo"
Leo.species = "Anemic"
Leo.date_added = "20200406"

Steven = Salmon()
Steven.name = "Steven"
Steven.species = "Rainbow Speckled"
Steven.date_added = "20190601"

George = Guppy()
George.name = "George"
George.species = "Flag Tail"
George.date_added = "20161108"

Kevin = Koi()
Kevin.name = "Kevin"
Kevin.species = "Neon Orange Glow"
Kevin.date_added = "20210309"

Omar = Oscar()
Omar.name = "Omar"
Omar.species = "Tuxedo Pink"
Omar.date_added = "20120919"

Billy = Bass()
Billy.name = "Billy"
Billy.species = "Large Mouth"
Billy.date_added = "20201215"



# after refactoring, use these to build new objects:
mary = Moose("Mary", "Alaskan", "Midday")
marvin = Moose("Marvin", "Great North Mainer", "Morning")
warren = Wildebeast("Warren", "Hornless", "Morning")
winnie = Wildebeast("Winnie", "Domesticated", "Afternoon")
colton = Cow("Colton", "Holstein", "Afternoon")
cullen = Cow("Cullen", "Angus Bull", "Midday")
genny = Gazelle("Genny", "Longhaired", "Midday")
gary = Gazelle("Gary", "Canadian", "Morning")
rex = Reindeer("Rex", "Hairless", "Monring")
rudolph = Reindeer("Rudolph", "Red-nosed", "Afternoon")
ned = Worm("Ned", "Nightcrawler")
golda = Slug("Golda", "Garden Slug")
colby = Cobra("Colby", "Congo")
aaron = Asp("Aaron", "Black Mamba")
lawrence = Leech("Lawrence", "Saltwater")
sara = Salmon("Sara", "Murrel")
gayle = Guppy("Gayle", "Basking")
keith = Koi("Keith", "Barb Tail")
oliver = Oscar("Oliver", "Beluga")
barry = Bass("Barry", "Small Mouth")
