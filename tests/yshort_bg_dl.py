from threading import Thread
from queue import Queue
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
import yt_dlp
from rich.console import Console
console = Console()


def status(x, **kwargs):
    return console.status(x, spinner='dots2', **kwargs)

# [...document.querySelectorAll(`ytd-rich-item-renderer`)].map(x => [x.querySelector('ytd-thumbnail a').href, x.querySelector('#video-title').textContent, x.querySelector('#time-status #text').textContent.trim()]).filter(x => {
#     console.log(x[2].split(":").map(Number))
#     let [hrs, mins, secs]  = x[2].split(":").map(Number)
#     if (secs == null) {
#         secs = mins
#         mins = hrs
#     }
#     return mins <= 4
# }) .map(x => `'${x[0]}', # ${x[1]} - ${x[2]}`).join("\n")

#fmt: off
videos = [
    # 'https://www.youtube.com/watch?v=ZzMbU5aOaxI', # Painting Squishy Ghost and Pumpkin #halloween #pumpkin #ghost #painting #sosatisfying  #crafting - 3:12
    # 'https://www.youtube.com/watch?v=hIRsb2D6bS4', # How to Carve a Pumpkin | ASMR #sosatisfying #halloween #satisfying #jackolantern #pumpkin - 4:04
    # 'https://www.youtube.com/watch?v=Vm4x9RBg0QU', # Satisfying Slime ASMR Compilation #sosatisfying #asmr #slimeasmr - 3:04
    # 'https://www.youtube.com/watch?v=VxeQ5p0AMJ8', # Bare Feet Squish Foam Filled Crocs | Satisfying Compilation #feet #crocs  #slime #shavingcream - 4:22
    # 'https://www.youtube.com/watch?v=A15jorL2xg0', # Food or Soap? Relaxing Soap Cutting Compilation | So Satisfying #nomusic #asmr #soapcutting - 4:23
    # 'https://www.youtube.com/watch?v=XTD29NyYCMw', # Best of Orbeez Compilation | So Satisfying #orbeez #asmr #satisfying - 4:28
    # 'https://www.youtube.com/watch?v=C-HKoJ29Iro', # Back to School ASMR Compilation | So Satisfying - 2:41
    # 'https://www.youtube.com/watch?v=dkxlfHriEuo', # ASMR Floral Foam Satisfying compilation (no music) | So Satisfying - 4:23
    # 'https://www.youtube.com/watch?v=K9UThVPe7wA', # ASMR Paint Roller compilation | So Satisfying - 4:05
    # 'https://www.youtube.com/watch?v=QxOCxADoNE8', # the most relaxing ASMR videos (no music) #asmr #satisfyingasmr #sosatisfying - 4:23
    # 'https://www.youtube.com/watch?v=VmjjvNCXq4k', # ASMR baking chip cookies | most satisfying #sosatisfying #satisfyingasmr #asmr #baking - 3:48
    # 'https://www.youtube.com/watch?v=R2B3ly49brs', # so satisfying ASMR compilation (no music) | RELAXING #satisfyingasmr #sosatisfying #satisfyingvideos - 3:31
    # 'https://www.youtube.com/watch?v=bc8Q9LsX0fU', # Crackling Marshmallow Fire Pit Roast ASMR #satisfyingasmr #marshmallow #satisfyingfoods - 3:15
    # 'https://www.youtube.com/watch?v=KzBcUNjZnY4', # super satisfying asmr food compilation - 4:20
    # 'https://www.youtube.com/watch?v=gfDgHOclvNI', # the most satisfying video you will ever watch - 4:17
    # 'https://www.youtube.com/watch?v=DIj9poLKcxU', # Do these videos put you to sleep? | So Satisfying asmr compilation - 4:24
    # 'https://www.youtube.com/watch?v=ZCnCXMbKgCs', # Honeycomb squeeze & more So Satisfying ASMR - 4:04
    # 'https://www.youtube.com/watch?v=9fRtlQseL74', # ultra satisfying asmr | paint squeezing - 4:17
    # 'https://www.youtube.com/watch?v=e2ZrQEYmbd4', # relaxing asmr compilation (no music) crunchy sounds - 4:15
    # 'https://www.youtube.com/watch?v=s6Sm_45dDiM', # super satisfying nonstop asmr & drawing - 4:08
    # 'https://www.youtube.com/watch?v=ak-vyVMeDfs', # slicing, squeezing, plucking | the most satisfying ASMR (no music) - 4:00
    # 'https://www.youtube.com/watch?v=hqxpxrOQPjo', # Satisfying hair pull & asmr no music - 3:59
    # 'https://www.youtube.com/watch?v=BajhMngtbas', # Super satisfying video (ASMR no MUSIC) - 3:58
    # 'https://www.youtube.com/watch?v=-dmGcGp44DI', # So Satisfying ASMR Video Compilation (Relaxing) (No Music) - 4:01
    # 'https://www.youtube.com/watch?v=xhtE9Zem4C4', # So Satisfying ASMR compilation video (No Music) RELAXING & CALMING - 3:40
    # 'https://www.youtube.com/watch?v=gySiMUTvtXg', # Super Satisfying Cheese Carve (asmr compilation) - 3:36
    # 'https://www.youtube.com/watch?v=q-J-XdDY-VM', # Best of So Satisfying (ASMR no music) - 3:52
    # 'https://www.youtube.com/watch?v=culjlCR4cGw', # Less-Mess Magic Sand - Satisfying Compilation - 1:05
    # 'https://www.youtube.com/watch?v=mbD48wqhyYo', # Super Satisfying video compilation (squeeze ASMR) - 3:59
    # 'https://www.youtube.com/watch?v=Ekp168IW_D8', # Super Satisfying Video Compilation (No Music) - 4:01
    # 'https://www.youtube.com/watch?v=ezb4EiJ9Upw', # So Satisfying ASMR video compilation (No Music) RELAXING - 4:04
    # 'https://www.youtube.com/watch?v=9ST_GPd4ecM', # Super Satisfying Video Compilation (no music) - 4:14
    # 'https://www.youtube.com/watch?v=eg6z2Lek2og', # Super Satisfying ASMR compilation RELAXING (No music) - 4:18
    # 'https://www.youtube.com/watch?v=mFQ7OjvQzzk', # Super Relaxing Satisfying Video (ASMR no music) - 4:22
    # 'https://www.youtube.com/watch?v=apjaPZU-48A', # Best Satisfying Compilation RELAXING - 4:19
    # 'https://www.youtube.com/watch?v=XQ8sGllzCIs', # DO you find these videos satisfying? ASMR satisfying video compilation - 4:15
    # 'https://www.youtube.com/watch?v=NtJ-PXsahKI', # So Satisfying ASMR video compilation (No Music) - 4:42
    # 'https://www.youtube.com/watch?v=DxFb7hysWvQ', # Satisfying Crush and Scrape ASMR - 4:57
    # 'https://www.youtube.com/watch?v=Pip8nIW9S4Q', # Satisfying ASMR compilation (SUPER RELAXING) - 4:51
    # 'https://www.youtube.com/watch?v=2YI1cGtHI_w', # BEST OF SO SATISFYING SNAPCHAT (RELAXING) - 2:37
    # 'https://www.youtube.com/watch?v=8mbCYNtzK-k', # So Satisfying ASMR video compilation (No Music) RELAXING FLORAL FOAM SQUEEZE - 2:37
    # 'https://www.youtube.com/watch?v=SKzcYHpj7-A', # Satisfying ASMR Hot tool compilation (RELAXING) - 2:38

#     'https://www.youtube.com/shorts/zz1nXR9dIEU', # "Skittles in Floral Foam #sosatisfying  #alecbenjamin #skittles #floralfoam #oddlysatisfying"
# 'https://www.youtube.com/shorts/-v0tghId0hw', # "Veggie Stick ASMR Crunch #satisfying #sosatisfying #relaxing #asmr #crunchy"
# 'https://www.youtube.com/shorts/7NpfE2HpGAA', # "Pulling Candle Wick #satisfying #sosatisfying #relaxing #candle #satisfyingvideos"
# 'https://www.youtube.com/shorts/1df7AZEoVZo', # "Tamping Down Colored Sand #satisfying #sosatisfying #sand #relaxing #visualasmr"
# 'https://www.youtube.com/shorts/dIN_GbJmwuE', # "Twirling Rainbow Glitter #sosatisfying #satisfying #glitter #rainbow #oddlysatisfying"
# 'https://www.youtube.com/shorts/oLd0oQTM5FY', # "Peeling Clay off Spiky Glove #sosatisfying #satisfyingvideos #oddlysatisfying #relax #clay #slime"
# 'https://www.youtube.com/shorts/ILUXlIt5Uaw', # "Green Slime Spike Pull #sosatisfying #slime #satisfyingvideos #oddlysatisfying #green #slimeasmr"
# 'https://www.youtube.com/shorts/wRQnMNmCm8Y', # "Hot Imprint on Foam Strawberry #satisfying #sosatisfying #relaxing #visualasmr #strawberry"
# 'https://www.youtube.com/shorts/Ny418OgaihY', # "Green Slime Syringe #satisfying #sosatisfying #slime #slimeasmr #green #oddlysatisfying"
# 'https://www.youtube.com/shorts/NlRGjNh9kpQ', # "Painting Nails Purple #satisfying #sosatisfying #oddlysatisfying #relaxing #purple #nailart #nails"
# 'https://www.youtube.com/shorts/UA28ktZ-TAo', # "Shaving Cream Foot Squish #sosatisfying #satisfying #oddlysatisfying #relaxing"
# 'https://www.youtube.com/shorts/ksEEyW9eW9A', # "Green Sand Scoop #satisfying #sosatisfying #green #sand #oddlysatisfying"
# 'https://www.youtube.com/shorts/lk7cf280rNk', # "Melting Orange and Black Lipstick #sosatisfying #halloween #melting #relaxing #oddlysatisfying"
# 'https://www.youtube.com/shorts/hil2wDTzDHQ', # "Carving Skeleton Candle #sosatisfying #skeleton #halloween #scary #candle #slicing"
# 'https://www.youtube.com/shorts/wYWSBgYJFXE', # "Blowing Out Halloween Candles #sosatisfying #candles #spooky #cozy #halloween #satisfyingvideos"
# 'https://www.youtube.com/shorts/ffNhZ8lzIC8', # "Pumpkin Stamp #sosatisfying #satisfyingvideos #stamping #pumpkin #halloween"
# 'https://www.youtube.com/shorts/QhPox7xsb6I', # "Painting Jack O’Lantern Face #sosatisfying #satisfyingvideos #pumpkin #halloween #painting"
# 'https://www.youtube.com/shorts/3YAhqSiHPiM', # "Red Dripping Skeleton Candle #sosatisfying #skeleton #halloween #candle #spooky #oddlysatisfying"
# 'https://www.youtube.com/shorts/LQcATuxyMMI', # "Painting Squishy Pumpkin #sosatisfying #halloween #orange #pumpkin #painting #satisfyingvideos"
# 'https://www.youtube.com/shorts/uz445mtMmVM', # "Painting RIP Gravestone #sosatisfying #oddlysatisfying #painting #halloween #scary #spooky"
# 'https://www.youtube.com/shorts/W2A5oc1MWzc', # "Painting Black Spider #halloween #spider #painting #sosatisfying #satisfying #relaxing #spooky"
# 'https://www.youtube.com/shorts/2mB8Pkn1QKI', # "Crushing Candy Eyeball #sosatisfying #oddlysatisfying #eyes #scary #halloween #candy #asmr"
# 'https://www.youtube.com/shorts/wY1xIiq06jk', # "Writing Happy Halloween #sosatisfying #satisfyingvideos #writing #halloween #fall #relax"
# 'https://www.youtube.com/shorts/wRuVfdOmeVo', # "Candy Corn Carve #carving #candy #halloween #cute #relaxing #soapcutting #visualasmr #sosatisfying"
# 'https://www.youtube.com/shorts/nyGxN2Xp3jA', # "Glowing Pumpkin Drawing #drawing #pumpkin #halloween #satisfying #sosatisfying"
# 'https://www.youtube.com/shorts/i44ZDEWgICI', # "BOO Painted Sign #sosatisfying #satisfyingvideos #oddlysatisfying #paint halloween #ghost"
# 'https://www.youtube.com/shorts/pukUCO6c1MY', # "Black and Orange Witch’s Cauldron #halloween #witch #spooky #sosatisfying #visualasmr"
# 'https://www.youtube.com/shorts/FEBzFSIC_AY', # "Crushing Pink Sand #sosatisfying #satisfyingvideos #satisfying #pink #sand #asmr #pyramid"
# 'https://www.youtube.com/shorts/5JBX8OArEAc', # "Green Soap Carve #sosatisfying #satisfyingvideos #oddlysatisfying #soapcutting #soap #green"
# 'https://www.youtube.com/shorts/KbOkVA8KNI0', # "Pulling Apart Egg Bun #sosatisfying #satisfying #satisfyingvideos #foodasmr #food"
# 'https://www.youtube.com/shorts/MEO5jFu5U6g', # "Crushing Soda Cans #sosatisfying #satisfyingvideos #oddlysatisfying #soda #crushing"
# 'https://www.youtube.com/shorts/gKRlhquCwt8', # "Pulling Green Slime #sosatisfying #satisfyingvideos #slime #asmr #slimeasmr #green"
# 'https://www.youtube.com/shorts/2AjOvek8fFI', # "Spiky Glove Clay Peel #sosatisfying #satisfyingvideos #oddlysatisfying #clay #peeling #blue #gloves"
# 'https://www.youtube.com/shorts/6-uvQlxG4K8', # "Red Rose Painted Black #sosatisfying #satisfyingvideos #rose #flower #paint"
# 'https://www.youtube.com/shorts/5W7cxQHYFRs', # "Red and White Slime #asmr #slime #slimeasmr #sosatisfying #satisfyingasmr #satisfyingvideos"
# 'https://www.youtube.com/shorts/KNL_Kg1Lw54', # "Carving Whale Soap #sosatisfying #soapcutting #soapasmr #satisfying #whale #asmr"
# 'https://www.youtube.com/shorts/TLXCZd-bLPY', # "Shaving Cream on Purple Floam #sosatisfying #floam #purple #shavingcream #asmr #satisfyingasmr"
# 'https://www.youtube.com/shorts/PtbI40LtOMI', # "Scalloped Clay Carving #blue #clay #carving #oddlysatisfying #sosatisfying #visualasmr"
# 'https://www.youtube.com/shorts/BBbNvW11yA4', # "Mirror Ball on Pink Sand Pyramid #sosatisfying #satisfying #pink #sand #relaxing"
# 'https://www.youtube.com/shorts/4-pVk4gT2Io', # "Strawberry Slicing ASMR #sosatisfying #satisfyingfood #asmr #strawberry #fruitcutting"
# 'https://www.youtube.com/shorts/06FAsS1N4hM', # "Glitter Glue in Floral Foam #sosatisfying #satisfyingvideos #floam #glitterglue #slime"
# 'https://www.youtube.com/shorts/az0lVlm2v5M', # "Pumpkin Watercolor Painting #sosatisfying #satisfying #painting #watercolor #pumpkin #halloween"
# 'https://www.youtube.com/shorts/cyGoGdBWkJM', # "Orbeez Glass Jar Smash #orbeez #blue #masonjar #sosatisfying #oddlysatisfying #satisfying"
# 'https://www.youtube.com/shorts/UROyPz5jju0', # "Ramen or Soap #asmr #soapcutting #ramen #foodasmr #sosatisfying #satisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/vvagMUN9AK8', # "Jawbreaker Dremel #jawbreaker #drill #candy #sosatisfying #oddlysatisfying #asmr  #satisfyingvideos"
# 'https://www.youtube.com/shorts/B7Lr1Z5U7II', # "Clay Potato Masher #sosatisfying #satisfying #oddlysatisfying #clay #clayart #slime"
# 'https://www.youtube.com/shorts/TRm1KwHvt9o', # "Green Slime  #sosatisfying #slime #slimeasmr #asmr #green #satisfying #satisfyingsounds"
# 'https://www.youtube.com/shorts/JDKY39Npf_o', # "Soda Pour in Cowboy Boot  #sosatisfying #satisfyingvideos #cowboys #mountaindew #asmr #soda"
# 'https://www.youtube.com/shorts/oYjSJOfhnmQ', # "Ring Pop Melt  #sosatisfying  #satisfyingvideos  #oddlysatisfying #ringpop #candy #melting"
# 'https://www.youtube.com/shorts/bhBjE1AuKpY', # "Spiky Soap Slicing #sosatisfying #soapcutting #soap #slicing #oddlysatisfying"
# 'https://www.youtube.com/shorts/nHEnN-f4sHA', # "Rainbow Soap Slicing #sosatisfying #rainbow #soapcutting #soap #asmr"
# 'https://www.youtube.com/shorts/19lYh4jVPwE', # "Water Dots on Expanding Sponge #sosatisfying #sponge #oddlysatisfying"
# 'https://www.youtube.com/shorts/f_BJNA7NAs0', # "Cutting Bacon Soap #sosatisfying #soapcutting #asmr #satisfying"
# 'https://www.youtube.com/shorts/ZmNMAEDCmN0', # "Demolding Ice Cubes #sosatisfying #oddlysatisfying #ice #icecube #asmr #demolding"
# 'https://www.youtube.com/shorts/ayceDYWDoUk', # "Making Iced Coffee #sosatisfying #coffee #icedcoffee #satisfyingasmr #asmr #satisfyingfood"
# 'https://www.youtube.com/shorts/wjjatuYjv9Q', # "Shaving Corn Soap #sosatisfying #soap #soapcutting #corn #oddlysatisfying #foodasmr"
# 'https://www.youtube.com/shorts/4ef0ofw-x6s', # "Balloon Animal Inflating #balloon #sosatisfying #reverse #satisfying  #satisfyingvideos"
# 'https://www.youtube.com/shorts/MeV-SgdY3p8', # "Blue Candle Carve #candle #candlecarving #soapcutting #sosatisfying #satisfying #blue"
# 'https://www.youtube.com/shorts/fdINuYw-7rM', # "Scraping Nerds off Ruler #sosatisfying #oddlysatisfying #candy #backtoschool"
# 'https://www.youtube.com/shorts/fnaQ1hyXJ04', # "Pink Sand Slice ASMR #sosatisfying #sand #pink #asmr #satisfyingasmr"
# 'https://www.youtube.com/shorts/KZIvl3_GGrM', # "Gold Spirograph Twirl  #sosatisfying #satisfyingart #sosatisfying #spirograph #art"
# 'https://www.youtube.com/shorts/DVWuyF8Y8rY', # "Stress Ball Squeeze #sosatisfying #satisfying #stressball #pineapple"
# 'https://www.youtube.com/shorts/JdAMJDVny50', # "Yellow Frosting Press #sosatisfying #satisfying #frosting #sprinkles"
# 'https://www.youtube.com/shorts/j6nsai7fbGQ', # "Dipping Donut in Purple Slime #slime #purple #donuts #sosatisfying #slimeasmr #oddlysatisfying"
# 'https://www.youtube.com/shorts/it1U6Y-fH30', # "Painting Rainbow Orb #sosatisfying #paint #rainbow #satisfyingvideos"
# 'https://www.youtube.com/shorts/n11gQzjlmH0', # "Pressing Jewels in Floral Foam #sosatisfying #satisfyingvideos #floralfoam #jewels"
# 'https://www.youtube.com/shorts/ujQaHz_3RfE', # "Colorful Care Bear Drawing #sosatisfying #satisfyingvideos #carebears #drawing #rainbow"
# 'https://www.youtube.com/shorts/X2qlTrOMK7w', # "Strawberry Candle Carving #sosatisfying #candle #candlecarving #strawberry"
# 'https://www.youtube.com/shorts/XhhV6oduWzs', # "Rose Quartz Soap Cutting #soapcutting #asmr #sosatisfying #soap"
# 'https://www.youtube.com/shorts/wzs7HiU5svg', # "Colorful Candy Crunch #asmr #candy #sosatisfying #satisfyingfood"
# 'https://www.youtube.com/shorts/2Mf7wJRKSyY', # "Gold Ink Swirl #sosatisfying #slomo #gold #paint #visualasmr"
# 'https://www.youtube.com/shorts/LE_3zapswns', # "Bacon Sizzling #asmr #bacon #sosatisfying #cooking"
# 'https://www.youtube.com/shorts/l2a1_30sHNo', # "Pink Sponge Inflates #sosatisfying #satisfyingvideos #sponge #pink"
# 'https://www.youtube.com/shorts/A-9XWuQ7uIo', # "Pumpkin Soap Carve #sosatisfying #pumpkin #halloween #soapcutting"
# 'https://www.youtube.com/shorts/UK6bMKjqREc', # "Happy Mushroom Drawing #art #drawing #sosatisfying #satisfying"
# 'https://www.youtube.com/shorts/n-UeK9RB8l8', # "Orbeez in Blue Glove  #sosatisfying #oddlysatisfying #orbeez #asmr"
# 'https://www.youtube.com/shorts/PODCvvmUHIQ', # "Orbeez in Slime #asmr #sosatisfying #orbeez #slimeasmr"
# 'https://www.youtube.com/shorts/05yMoxDf5dw', # "Pumpkin Candle Carve #sosatisfying #pumpkin #candle #halloween"
# 'https://www.youtube.com/shorts/OtA1Uo_Z9x4', # "Rainbow Sock Foam Squeeze #oddlysatisfying #foam #rainbow #sosatisfying"
# 'https://www.youtube.com/shorts/KEdD5NUgfV4', # "Blue Orbeez Balloon Pop #sosatisfying #oddlysatisfying #orbeez  #satisfyingvideos"
# 'https://www.youtube.com/shorts/Dcljl_qqFqQ', # "Colorful Pom Pom Soap Carve #sosatisfying #soapcutting #asmr"
# 'https://www.youtube.com/shorts/gektVrnNOXs', # "Orange Earplug Smush #sosatisfying #oddlysatisfying #orange"
# 'https://www.youtube.com/shorts/USqoQ9PKaqI', # "Green Powder in Slime #sosatisfying #asmr #slime #green"
# 'https://www.youtube.com/shorts/o17zwP0hyno', # "Glittery Makeup Brush Twirl #sosatisfying #satisfyingvideos #glitter #purple"
# 'https://www.youtube.com/shorts/XAAQmuVVeDE', # "Breaking Creme Brulee #satisfyingfood #cremebrulee #asmr"
# 'https://www.youtube.com/shorts/ydnNX60UJ3k', # "Pop Rocks in Soda #asmr #soda #sosatisfying #satsifyingasmr"
# 'https://www.youtube.com/shorts/x4-X-FPdqrM', # "Multicolor Clay Carve #sosatisfying #art #carving #clay"
# 'https://www.youtube.com/shorts/W4LIlFYP71k', # "Hot Knife Slices Toothbrushes #oddlysatisfying #sosatisfying"
# 'https://www.youtube.com/shorts/2QSl4craScM', # "Lipstick in Slime #sosatisfying #satisfyingvideos #slimeasmr #slime"
# 'https://www.youtube.com/shorts/2sHJM76K7Iw', # "Stepping on Water Balloons #sosatisfying #oddlysatisfying #balloon"
# 'https://www.youtube.com/shorts/pYm9uNvT0p8', # "Blue Slime Pour #sosatisfying #satisfyingvideos #slime"
# 'https://www.youtube.com/shorts/WmNL8Zo3sbU', # "Reverse Rainbow Butter Scoop  #satisfyingvideos #sosatisfying #bodybutter  #rainbow"
# 'https://www.youtube.com/shorts/RsgjJ2orMSw', # "Sparkly Eyeshadow Destroyed #makeup #eyeshadow #satisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/qlck6DsiSWE', # "Magnetic Slime #sosatisfying #slime #magnet"
# 'https://www.youtube.com/shorts/VAJDB3L81wY', # "Gallium Melts Slime in Dragonfruit  #sosatisfying #oddlysatisfying #slime #gallium"
# 'https://www.youtube.com/shorts/NDIhLonLWfw', # "Pink Clay Balls Squished #sosatisfying #asmr #clay"
# 'https://www.youtube.com/shorts/GH4WLgzfAvs', # "Hot Wire Slices Straws #sosatisfying #oddlysatisfying #rainbow"
# 'https://www.youtube.com/shorts/zGbjjznB2-g', # "Painting Red Circle #sosatisfying #painting #watercolor"
# 'https://www.youtube.com/shorts/zRpcHl7vdno', # "Pink Slime in Egg Slicer #sosatisfying #oddlysatisfying #slime #pink"
# 'https://www.youtube.com/shorts/d_ZBwP9CBko', # "Golden Candle Carve #satisfyingvideos #sosatisfying #soapcarving"
# 'https://www.youtube.com/shorts/nRJw6_E9Ek8', # "Tree Watercolor Painting #sosatisfying #nature #watercolor #painting"
# 'https://www.youtube.com/shorts/U5YpB1OirKo', # "Destroying Sand Rainbow #rainbow #sandart #sosatisfying"
# 'https://www.youtube.com/shorts/6ueaLcYh810', # "Carving Green Lipstick #lipstick #green #sosatisfying #carving"
# 'https://www.youtube.com/shorts/m_NFznzRuUc', # "September Gel Pen Writing #sosatisfying #autumn #satisfyingvideos #september"
# 'https://www.youtube.com/shorts/5_bwE1FZiBE', # "Drawing Hearts with Gel Pen #sosatisfying #drawing #heart"
# 'https://www.youtube.com/shorts/nmryGOceOAE', # "Cutting Acorn Soap #soapcutting #sosatisfying #satisfying"
# 'https://www.youtube.com/shorts/2SbvrNw2kyY', # "Purple Glitter Shaving Cream Squish #sosatisfying #shavingcream #glitter #satisfyingvideos"
# 'https://www.youtube.com/shorts/Lf1-oGCne1o', # "Pink Soap Cut ASMR #sosatisfying #soapcutting #satisfyingasmr #pink"
# 'https://www.youtube.com/shorts/EtFzh5WYelE', # "Hot Metal Ball in Slime #sosatisfying #slime #green #asmr"
# 'https://www.youtube.com/shorts/9a3QGD5q_r4', # "Filling Heart Mold with Rainbow Paint #sosatisfying #paint #satisfying #hearts"
# 'https://www.youtube.com/shorts/bbEVa2o5xZM', # "Crushing Dot Candy #candy #sosatisfying #satisfyingfood #colorful"
# 'https://www.youtube.com/shorts/h0I9vQwX8DQ', # "Comb Pops Foam-Filled Glove #oddlysatisfying #foam #sosatisfying"
# 'https://www.youtube.com/shorts/EJqk0GnqpV8', # "Hot Knife Carves Blue Soap #soapcutting #sosatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/QviERDvpuyo', # "Ocean Washes Sand Heart Away  #sosatisfying #ocean #sand #oceanwaves"
# 'https://www.youtube.com/shorts/4B7rNOpVoAI', # "Destroying Blue Lipstick #sosatisfying #oddlysatisfying #lipstick"
# 'https://www.youtube.com/shorts/7PeMwm7jXr0', # "Canned Latte Pour #sosatisfying #asmr #latte"
# 'https://www.youtube.com/shorts/zygyI_d23Xg', # "Purple and Green Orbeez Explosion #sosatisfying #orbeez #satisfyingvideos"
# 'https://www.youtube.com/shorts/Ur8cegOSNuA', # "Glittery Flowers Paint Roller Scrape #satisfyingvideos #oddlysatisfying #paintroller"
# 'https://www.youtube.com/shorts/Ik1Ko33kPe8', # "Hot Ball Melts Pool Noodle #sosatisfying #oddlysatisfying #satisfying"
# 'https://www.youtube.com/shorts/5riRthOpHSk', # "Scooping Dragonfruit #sosatisfying #satisfyingvideos #satisfyingfood #dragonfruit"
# 'https://www.youtube.com/shorts/9MrHRW-n5R0', # "Pink Fidget Toy Explosion #satisfyingvideos #oddlysatisfying #fidget #sosatisfying"
# 'https://www.youtube.com/shorts/n2PEk4vcpig', # "Blue Orbeez Squeeze & Scrape #sosatisfying #satisfyingvideos #orbeez"
# 'https://www.youtube.com/shorts/VIbSKvLN-E8', # "Purple Orbeez Rolling Pin #sosatisfying #oddlysatisfying #purple #orbeez"
# 'https://www.youtube.com/shorts/NORAUWzcqEg', # "Scissors Cutting Purple Slime #asmr #sosatisfying #slime #slimeasmr"
# 'https://www.youtube.com/shorts/06IyroPbzZA', # "Reverse Marshmallow Burn #sosatisfying #satisfyingfoods #marshmallow"
# 'https://www.youtube.com/shorts/rRPAgqriM9U', # "Cutting Colorful Sand Molds #sosatisfying #satisfying #kineticsand"
# 'https://www.youtube.com/shorts/WfiIgRyq4VU', # "Pulling Pencils From Water-Filled Bag#sosatisfying #oddlysatisfying #pencil #water"
# 'https://www.youtube.com/shorts/kzU2RVgeLMs', # "Colorful Goggle Paint Press #sosatisfying #paint #satisfyingart"
# 'https://www.youtube.com/shorts/TKS00YIo4rg', # "Pink Balloon Popping #sosatisfying #satisfyingvideos #balloon"
# 'https://www.youtube.com/shorts/URJjEDnGx2E', # "Epic Blue Balloon Pop #balloon #sosatisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/Xonl8j1wTE8', # "Glittery Pink Water Toy Pop #sosatisfying #fidgettoy #oddlysatisfying"
# 'https://www.youtube.com/shorts/M-qacf6GWDw', # "Nemo Soap Cutting #sosatisfying #asmr #soapcutting"
# 'https://www.youtube.com/shorts/8QtSDt8Xx0g', # "Crackling Eggshells ASMR #sosatisfying #tingles #eggshell #oddlysatisfying"
# 'https://www.youtube.com/shorts/BuncNIsY77s', # "Tingly Slime and Floam Chop #satisfyingvideos #asmr #slime #floam"
# 'https://www.youtube.com/shorts/IFYUNqEYJbs', # "Rainbow Tool Presses Shaving Cream #sosatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/wm-OiFZJdtg', # "Shoe Popping Clay #sosatisfying #clay #satisfying"
# 'https://www.youtube.com/shorts/Q-E8BkFRVdU', # "Pink Slime in Green Net #sosatisfying #slime #oddlysatisfying"
# 'https://www.youtube.com/shorts/3C4y20tL2pM', # "Sparkly Pink Squish Toy Pop #sosatisfying #satisfyingvideos #oddlysatisfying"
# 'https://www.youtube.com/shorts/IXPxZdOY24s', # "Crunching Leaves ASMR #sosatisfying #asmr #satisfyingasmr"
# 'https://www.youtube.com/shorts/rp979uVG_58', # "Blue Sand Chop ASMR #sosatisfying #satisfyingasmr"
# 'https://www.youtube.com/shorts/eMifCaO0CW0', # "Orange Jelly Squish #sosatisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/M7mf3XBH10U', # "Pink and Green Sand Squish #sosatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/OHuK-s12I1k', # "Colorful Wet Sponge Squeeze #sosatisfying #sponge #asmrsounds"
# 'https://www.youtube.com/shorts/Qi_tdt_tYBA', # "Blue Orbeez Garlic Press Squish #orbeez #oddlysatisfying"
# 'https://www.youtube.com/shorts/kFQhOQX7qKc', # "Tingly Pink Clay Peel ASMR #satisfyingvideos #satisfyingasmr"
# 'https://www.youtube.com/shorts/JwaKFwcEyho', # "Box Cutter Slices Clear Lipstick #sosatisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/1tu7T-TtUfA', # "mesmerizing blue sand scoop #sosatisfying #satisfying"
# 'https://www.youtube.com/shorts/6uCQRfayJb4', # "tiny mic on plastic glove ASMR #satisfyingvideos #sosatisfying"
# 'https://www.youtube.com/shorts/Fl1KTYKHCsk', # "Blue Food Coloring in Oil #satisfyingvideos #oddlysatisfying"
# 'https://www.youtube.com/shorts/pe_2U63tOUc', # "tingly bath bomb chop ASMR #sosatisfying #oddlysatisfying #bathbomb"
# 'https://www.youtube.com/shorts/OjPgn6x7hKE', # "crunchy croissant slicing ASMR #asmr #sosatisfying"
# 'https://www.youtube.com/shorts/7w-c8cc-BpQ', # "soothing silver candle peel #sosatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/ikrKk_DeWr4', # "Wait For The Reverse.. #sosatisfying #shorts"
# 'https://www.youtube.com/shorts/JUSttQg7OAk', # "just like a pimple  #sosatisfying  #oddlysatisfying"
# 'https://www.youtube.com/shorts/sRXfEXmrMUY', # "melting ASMR #sosatisfying #asmr #shorts"
# 'https://www.youtube.com/shorts/UzpEttsPRu4', # "the smoothest icing ever #sosatisfying #shorts"
# 'https://www.youtube.com/shorts/21IsRVBdqaM', # "Drawing Rainbow Hearts #satisfyingart #sosatisfying"
# 'https://www.youtube.com/shorts/2q-GiLVK7BE', # "Pins Placed in Foil ASMR #oddlysatisfying #sosatisfying #asmr"
# 'https://www.youtube.com/shorts/z7_pNIVs4gE', # "Satisfying Kiwi Slicer #sosatisfying #satisfyingfood"
# 'https://www.youtube.com/shorts/u8f56DLuRMw', # "Crunchy Glue Peel ASMR #sosatisfying #asmr #oddlysatisfying"
# 'https://www.youtube.com/shorts/_nlZOa_W57w', # "French Fry Pop It ASMR #satisfyingasmr #asmr #satisfyingsounds"
# 'https://www.youtube.com/shorts/igGGD9vWUyo', # "Triple Scissors Cutting Clay #sosatisfying #satisfyingvideo #clay"
# 'https://www.youtube.com/shorts/y4nTVLoerAE', # "Pink Balloon Pops #sosatisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/cnSXNtu16gA', # "Hot Pink Slime Squeeze #slime #slimeasmr #sosatisfying"
# 'https://www.youtube.com/shorts/oMgzsZJUXRc', # "Yellow Chalkboard Stars ASMR #sosatisfying #satisfyingart #asmr"
# 'https://www.youtube.com/shorts/rgoZIKT8rTc', # "Crunching Chips ASMR #sosatisfying #pringles #satisfyingfood"
# 'https://www.youtube.com/shorts/RDAGIBHWYO0', # "Pink Stress Ball Squeeze #sosatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/S_9gqx5-b-Y', # "Crushing Rice Krispy Cereal ASMR #sosatisfying #asmr #foodasmr"
# 'https://www.youtube.com/shorts/RIJfIrkiOuw', # "Sandle Soap Chopping ASMR #soapcutting #sosatisfying #asmr"
# 'https://www.youtube.com/shorts/sOhF9cvCk9U', # "Relaxing Rain Thunderstorm ASMR #satisfyingvideos #asmr #thunderstorm"
# 'https://www.youtube.com/shorts/KNFlp7PWaWk', # "Popping Red Currant Fruit #oddlysatisfying #foodasmr #sosatisfying"
# 'https://www.youtube.com/shorts/WevlehSZGNY', # "ASMR Drawing Yellow Chalk Stars #asmr #sosatisfying #satisfyingasmr"
# 'https://www.youtube.com/shorts/XdSQywCuJwU', # "Hot Metal in Blue Slime #slime #sosatisfying #satisfyingasmr"
# 'https://www.youtube.com/shorts/RVEhNjVFd2w', # "Pink Slime Squeeze #sosatisfying #slimeasmr #pink"
# 'https://www.youtube.com/shorts/TKAoZdf7OGM', # "Snipping Dead Flowers ASMR #sosatisfying #satisfyingasmr #flowers"
# 'https://www.youtube.com/shorts/MQTDhgo6RDk', # "Green Yarn Hot Knife Slice #green #sosatisfying #satisfying"
# 'https://www.youtube.com/shorts/xtVYnGkzA88', # "Glittery Paint Colander Press #oddlysatisfying #satisfyingvideos"
# 'https://www.youtube.com/shorts/AKVcVxFaN1U', # "Rainbow Slime Press #asmr #sosatisfying #slime"
# 'https://www.youtube.com/shorts/hnMphreuzso', # "ASMR Charm Cereal Crush #sosatisfying #satisfyingasmr #asmr"
# 'https://www.youtube.com/shorts/RP_tsJzEjVo', # "Purple Glitter Croc Foam Squish #sosatisfying #foam #satisfyingvideos"
# 'https://www.youtube.com/shorts/9FOUpS4m_-s', # "Blue Orbeez Cup Pour #sosatisfying #orbeez #satisfyingvideos"
# 'https://www.youtube.com/shorts/edjRtAfb0H4', # "Epic Foamy Blue Balloon Pop #sosatisfying #oddlysatisfying"
# 'https://www.youtube.com/shorts/FmyWqiFKUDI', # "Pink Paint Roller Scrape #sosatisfying #satisfyingvideos #barbie #barbiemovie"
# 'https://www.youtube.com/shorts/4NCRH4Fp3BE', # "Mesmerizing Soap Carve #soapcutting #sosatisfying #soap"
# 'https://www.youtube.com/shorts/jxqhTaQj3y0', # "Reverse Cotton Candy Melt #sosatisfying #satisfyingvideos #satisfyingfood"
# 'https://www.youtube.com/shorts/QHQh4GKLNPo', # "Jello Scoop Garlic Press #sosatisfying #oddlysatisfying #satisfying"
# 'https://www.youtube.com/shorts/zmRwGwfVZMU', # "Hot Bristle Brush Slice #oddlysatisfying #satisfying #sosatisfying"
# 'https://www.youtube.com/shorts/uhVrhA0U4fs', # "Crackling Croissant ASMR #tingles #sosatisfying #satisfyingasmr"
# 'https://www.youtube.com/shorts/-rh1MFMK_fc', # "Reverse Toothpaste Squeeze #oddlysatisfying #sosatisfying"
# 'https://www.youtube.com/shorts/4a9kkSUU_WE', # "Coffee Milk Pour #sosatisfying #satisfyingfood #coffee"
# 'https://www.youtube.com/shorts/tPLqT4WVMZY', # "Coloring Cloud ASMR #sosatisfying #satisfyingart #drawing"
# 'https://www.youtube.com/shorts/SF_LryNEbU8', # "ASMR Candy Chop #sosatisfying #oddlysatisfying #asmr"


  [
    "https://www.youtube.com/shorts/-v0tghId0hw",
    "Veggie Stick ASMR Crunch #satisfying #sosatisfying #relaxing #asmr #crunchy",
    "4.1K views"
  ],
  [
    "https://www.youtube.com/shorts/zz1nXR9dIEU",
    "Skittles in Floral Foam #sosatisfying #alecbenjamin #skittles #floralfoam #oddlysatisfying",
    "5.4K views"
  ],
  [
    "https://www.youtube.com/shorts/dIN_GbJmwuE",
    "Twirling Rainbow Glitter #sosatisfying #satisfying #glitter #rainbow #oddlysatisfying",
    "9.8K views"
  ],
  [
    "https://www.youtube.com/shorts/ksEEyW9eW9A",
    "Green Sand Scoop #satisfying #sosatisfying #green #sand #oddlysatisfying",
    "394 views"
  ],
  [
    "https://www.youtube.com/shorts/UA28ktZ-TAo",
    "Shaving Cream Foot Squish #sosatisfying #satisfying #oddlysatisfying #relaxing",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/5JBX8OArEAc",
    "Green Soap Carve #sosatisfying #satisfyingvideos #oddlysatisfying #soapcutting #soap #green",
    "11K views"
  ],
  [
    "https://www.youtube.com/shorts/KNL_Kg1Lw54",
    "Carving Whale Soap #sosatisfying #soapcutting #soapasmr #satisfying #whale #asmr",
    "3.5K views"
  ],
  [
    "https://www.youtube.com/shorts/PtbI40LtOMI",
    "Scalloped Clay Carving #blue #clay #carving #oddlysatisfying #sosatisfying #visualasmr",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/TLXCZd-bLPY",
    "Shaving Cream on Purple Floam #sosatisfying #floam #purple #shavingcream #asmr #satisfyingasmr",
    "678 views"
  ],
  [
    "https://www.youtube.com/shorts/BBbNvW11yA4",
    "Mirror Ball on Pink Sand Pyramid #sosatisfying #satisfying #pink #sand #relaxing",
    "36K views"
  ],
  [
    "https://www.youtube.com/shorts/B7Lr1Z5U7II",
    "Clay Potato Masher #sosatisfying #satisfying #oddlysatisfying #clay #clayart #slime",
    "7.2K views"
  ],
  [
    "https://www.youtube.com/shorts/bhBjE1AuKpY",
    "Spiky Soap Slicing #sosatisfying #soapcutting #soap #slicing #oddlysatisfying",
    "754 views"
  ],
  [
    "https://www.youtube.com/shorts/nHEnN-f4sHA",
    "Rainbow Soap Slicing #sosatisfying #rainbow #soapcutting #soap #asmr",
    "846 views"
  ],
  [
    "https://www.youtube.com/shorts/OtA1Uo_Z9x4",
    "Rainbow Sock Foam Squeeze #oddlysatisfying #foam #rainbow #sosatisfying",
    "3.3K views"
  ],
  [
    "https://www.youtube.com/shorts/KEdD5NUgfV4",
    "Blue Orbeez Balloon Pop #sosatisfying #oddlysatisfying #orbeez #satisfyingvideos",
    "3.8K views"
  ],
  [
    "https://www.youtube.com/shorts/x4-X-FPdqrM",
    "Multicolor Clay Carve #sosatisfying #art #carving #clay",
    "769 views"
  ],
  [
    "https://www.youtube.com/shorts/2sHJM76K7Iw",
    "Stepping on Water Balloons #sosatisfying #oddlysatisfying #balloon",
    "5.2K views"
  ],
  [
    "https://www.youtube.com/shorts/2QSl4craScM",
    "Lipstick in Slime #sosatisfying #satisfyingvideos #slimeasmr #slime",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/W4LIlFYP71k",
    "Hot Knife Slices Toothbrushes #oddlysatisfying #sosatisfying",
    "2K views"
  ],
  [
    "https://www.youtube.com/shorts/WmNL8Zo3sbU",
    "Reverse Rainbow Butter Scoop #satisfyingvideos #sosatisfying #bodybutter #rainbow",
    "4.7K views"
  ],
  [
    "https://www.youtube.com/shorts/pYm9uNvT0p8",
    "Blue Slime Pour #sosatisfying #satisfyingvideos #slime",
    "2.2K views"
  ],
  [
    "https://www.youtube.com/shorts/NDIhLonLWfw",
    "Pink Clay Balls Squished #sosatisfying #asmr #clay",
    "2.9K views"
  ],
  [
    "https://www.youtube.com/shorts/zRpcHl7vdno",
    "Pink Slime in Egg Slicer #sosatisfying #oddlysatisfying #slime #pink",
    "4.6K views"
  ],
  [
    "https://www.youtube.com/shorts/GH4WLgzfAvs",
    "Hot Wire Slices Straws #sosatisfying #oddlysatisfying #rainbow",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/qlck6DsiSWE",
    "Magnetic Slime #sosatisfying #slime #magnet",
    "3.6K views"
  ],
  [
    "https://www.youtube.com/shorts/VAJDB3L81wY",
    "Gallium Melts Slime in Dragonfruit #sosatisfying #oddlysatisfying #slime #gallium",
    "6.8K views"
  ],
  [
    "https://www.youtube.com/shorts/d_ZBwP9CBko",
    "Golden Candle Carve #satisfyingvideos #sosatisfying #soapcarving",
    "493 views"
  ],
  [
    "https://www.youtube.com/shorts/2SbvrNw2kyY",
    "Purple Glitter Shaving Cream Squish #sosatisfying #shavingcream #glitter #satisfyingvideos",
    "5.5K views"
  ],
  [
    "https://www.youtube.com/shorts/Lf1-oGCne1o",
    "Pink Soap Cut ASMR #sosatisfying #soapcutting #satisfyingasmr #pink",
    "2.4K views"
  ],
  [
    "https://www.youtube.com/shorts/EJqk0GnqpV8",
    "Hot Knife Carves Blue Soap #soapcutting #sosatisfying #satisfyingvideos",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/Ur8cegOSNuA",
    "Glittery Flowers Paint Roller Scrape #satisfyingvideos #oddlysatisfying #paintroller",
    "2.2K views"
  ],
  [
    "https://www.youtube.com/shorts/Ik1Ko33kPe8",
    "Hot Ball Melts Pool Noodle #sosatisfying #oddlysatisfying #satisfying",
    "4.1K views"
  ],
  [
    "https://www.youtube.com/shorts/n2PEk4vcpig",
    "Blue Orbeez Squeeze & Scrape #sosatisfying #satisfyingvideos #orbeez",
    "2.6K views"
  ],
  [
    "https://www.youtube.com/shorts/9MrHRW-n5R0",
    "Pink Fidget Toy Explosion #satisfyingvideos #oddlysatisfying #fidget #sosatisfying",
    "558 views"
  ],
  [
    "https://www.youtube.com/shorts/06IyroPbzZA",
    "Reverse Marshmallow Burn #sosatisfying #satisfyingfoods #marshmallow",
    "2.3K views"
  ],
  [
    "https://www.youtube.com/shorts/M-qacf6GWDw",
    "Nemo Soap Cutting #sosatisfying #asmr #soapcutting",
    "5K views"
  ],
  [
    "https://www.youtube.com/shorts/Xonl8j1wTE8",
    "Glittery Pink Water Toy Pop #sosatisfying #fidgettoy #oddlysatisfying",
    "2.6K views"
  ],
  [
    "https://www.youtube.com/shorts/IFYUNqEYJbs",
    "Rainbow Tool Presses Shaving Cream #sosatisfying #satisfyingvideos",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/Q-E8BkFRVdU",
    "Pink Slime in Green Net #sosatisfying #slime #oddlysatisfying",
    "4.4K views"
  ],
  [
    "https://www.youtube.com/shorts/IXPxZdOY24s",
    "Crunching Leaves ASMR #sosatisfying #asmr #satisfyingasmr",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/rp979uVG_58",
    "Blue Sand Chop ASMR #sosatisfying #satisfyingasmr",
    "815 views"
  ],
  [
    "https://www.youtube.com/shorts/M7mf3XBH10U",
    "Pink and Green Sand Squish #sosatisfying #satisfyingvideos",
    "1.6K views"
  ],
  [
    "https://www.youtube.com/shorts/Qi_tdt_tYBA",
    "Blue Orbeez Garlic Press Squish #orbeez #oddlysatisfying",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/JwaKFwcEyho",
    "Box Cutter Slices Clear Lipstick #sosatisfying #oddlysatisfying",
    "3.5K views"
  ],
  [
    "https://www.youtube.com/shorts/1tu7T-TtUfA",
    "mesmerizing blue sand scoop #sosatisfying #satisfying",
    "2.9K views"
  ],
  [
    "https://www.youtube.com/shorts/7w-c8cc-BpQ",
    "soothing silver candle peel #sosatisfying #satisfyingvideos",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/ikrKk_DeWr4",
    "Wait For The Reverse.. #sosatisfying #shorts",
    "1.5K views"
  ],
  [
    "https://www.youtube.com/shorts/JUSttQg7OAk",
    "just like a pimple #sosatisfying #oddlysatisfying",
    "2.3K views"
  ],
  [
    "https://www.youtube.com/shorts/sRXfEXmrMUY",
    "melting ASMR #sosatisfying #asmr #shorts",
    "2.6K views"
  ],
  [
    "https://www.youtube.com/shorts/cnSXNtu16gA",
    "Hot Pink Slime Squeeze #slime #slimeasmr #sosatisfying",
    "628 views"
  ],
  [
    "https://www.youtube.com/shorts/RDAGIBHWYO0",
    "Pink Stress Ball Squeeze #sosatisfying #satisfyingvideos",
    "1.5K views"
  ],
  [
    "https://www.youtube.com/shorts/RIJfIrkiOuw",
    "Sandle Soap Chopping ASMR #soapcutting #sosatisfying #asmr",
    "2K views"
  ],
  [
    "https://www.youtube.com/shorts/RVEhNjVFd2w",
    "Pink Slime Squeeze #sosatisfying #slimeasmr #pink",
    "784 views"
  ],
  [
    "https://www.youtube.com/shorts/XdSQywCuJwU",
    "Hot Metal in Blue Slime #slime #sosatisfying #satisfyingasmr",
    "2K views"
  ],
  [
    "https://www.youtube.com/shorts/MQTDhgo6RDk",
    "Green Yarn Hot Knife Slice #green #sosatisfying #satisfying",
    "1.5K views"
  ],
  [
    "https://www.youtube.com/shorts/RP_tsJzEjVo",
    "Purple Glitter Croc Foam Squish #sosatisfying #foam #satisfyingvideos",
    "1.3K views"
  ],
  [
    "https://www.youtube.com/shorts/edjRtAfb0H4",
    "Epic Foamy Blue Balloon Pop #sosatisfying #oddlysatisfying",
    "2.3K views"
  ],
  [
    "https://www.youtube.com/shorts/FmyWqiFKUDI",
    "Pink Paint Roller Scrape #sosatisfying #satisfyingvideos #barbie #barbiemovie",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/4NCRH4Fp3BE",
    "Mesmerizing Soap Carve #soapcutting #sosatisfying #soap",
    "628 views"
  ],
  [
    "https://www.youtube.com/shorts/jxqhTaQj3y0",
    "Reverse Cotton Candy Melt #sosatisfying #satisfyingvideos #satisfyingfood",
    "716 views"
  ],
  [
    "https://www.youtube.com/shorts/-rh1MFMK_fc",
    "Reverse Toothpaste Squeeze #oddlysatisfying #sosatisfying",
    "5.4K views"
  ],
  [
    "https://www.youtube.com/shorts/zmRwGwfVZMU",
    "Hot Bristle Brush Slice #oddlysatisfying #satisfying #sosatisfying",
    "1.9K views"
  ],
  [
    "https://www.youtube.com/shorts/SF_LryNEbU8",
    "ASMR Candy Chop #sosatisfying #oddlysatisfying #asmr",
    "5.8K views"
  ],
  [
    "https://www.youtube.com/shorts/s5MQP4T1G5A",
    "Epic Stress Ball Foam Pop #sosatisfying #satisfyingvideos",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/SbtSx6-VooY",
    "Purple Glitter Foam Croc Squish #sosatisfying #oddlysatisfying #satisfyingvideos",
    "6.7K views"
  ],
  [
    "https://www.youtube.com/shorts/WWMyggXG9bE",
    "Purple Glitter Squeeze #shorts #oddlysatisfying #glitter",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/MY5MtXXu3Vg",
    "Ultra Satisfying Purple Soap Carve #sosatisfying",
    "2.9K views"
  ],
  [
    "https://www.youtube.com/shorts/PHhP2AA2d70",
    "Pink Soap Tool Carve #oddlysatisfying #sosatisfying",
    "3K views"
  ],
  [
    "https://www.youtube.com/shorts/KUPS-3od6zU",
    "Star Sand Slice ASMR #satisfyingasmr #sosatisfying",
    "5K views"
  ],
  [
    "https://www.youtube.com/shorts/6eCe82hPSDE",
    "Syrupy Waffle Holographic Chop #oddlysatisfying #satisfyingfood #satisfying",
    "2.2K views"
  ],
  [
    "https://www.youtube.com/shorts/26Q2dGuEDfM",
    "Rubber Duck Soap Slice #soap #satisfyingasmr",
    "2.5K views"
  ],
  [
    "https://www.youtube.com/shorts/VSpi0rIrbYQ",
    "Sticky Green Sand Scoop #sosatisfying #satisfyingvideos",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/4xPHCpprJ1s",
    "Hot Knife Crayon Melt #sosatisfying #satisfyingart",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/MEHLhXzC0qA",
    "ASMR Black Soap Carve #satisfyingasmr #sosatisfying",
    "3.2K views"
  ],
  [
    "https://www.youtube.com/shorts/k41w1WJziII",
    "Hot Metal Styrofoam Melt #satisfying #sosatisfying",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/EOQWAx-YUQE",
    "Blue Starfish Soap Peel #sosatisfying #satisfyingvideos",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/J_wlXid4qew",
    "Blue Chalk Heart Crush #satisfyingvideos #oddlysatisfying",
    "10K views"
  ],
  [
    "https://www.youtube.com/shorts/L2xit-wJRYU",
    "Purple Clay Press #sosatisfying #satisfyingvideos",
    "2.2K views"
  ],
  [
    "https://www.youtube.com/shorts/8vlFvxMRwzI",
    "Blue Slime Oozing #oddlysatisfying #satisfying",
    "2.3K views"
  ],
  [
    "https://www.youtube.com/shorts/Sswh-L-3SYI",
    "Chalk Powder Explosion #sosatisfying #satisfyingvideos",
    "1.9K views"
  ],
  [
    "https://www.youtube.com/shorts/XvqO6m6Gtls",
    "Glass Orb Crushes Sand Pyramid #sosatisfying #satisfyingvideos",
    "1.2K views"
  ],
  [
    "https://www.youtube.com/shorts/shB1_mwWYtc",
    "Red Match Lit on Fire #satisfyingvideos # #sosatisfying",
    "912 views"
  ],
  [
    "https://www.youtube.com/shorts/10Rew2irF_I",
    "Green Sand Cube Slice #sosatisfying #satisfyingvideos",
    "2.4K views"
  ],
  [
    "https://www.youtube.com/shorts/FZVdpRyziHg",
    "Satisfying Reverse Holographic Slice",
    "846 views"
  ],
  [
    "https://www.youtube.com/shorts/hnHMkPEkdUU",
    "Ultra Satisfying Sand Combing #satisfyingvideos #oddlysatisfying",
    "1.7K views"
  ],
  [
    "https://www.youtube.com/shorts/zNsAMSuQGQI",
    "Satisfying Gold Paint Scrape #satisfyingvideos #sosatisfying",
    "3.9K views"
  ],
  [
    "https://www.youtube.com/shorts/lo7dhJs3mnA",
    "Satisfying Spiky Paint Pop #satisfyingvideos #shorts",
    "3.6K views"
  ],
  [
    "https://www.youtube.com/shorts/tjMDCzjZ9qQ",
    "Satisfying Chalk Puff in Reverse #sosatisfying #oddlysatisfying",
    "2.5K views"
  ],
  [
    "https://www.youtube.com/shorts/bbiP-IjvxJY",
    "Mesmerizing Wax Melt #sosatisfying #satisfyingvideos",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/_LG4mzaRJsE",
    "Relaxing Foam Squeeze #sosatisfying #satisfyingvideos",
    "1K views"
  ],
  [
    "https://www.youtube.com/shorts/Hfu3YVpWy2Q",
    "Delicious Honeycomb ASMR",
    "1.4K views"
  ],
  [
    "https://www.youtube.com/shorts/Y8xePsydrcs",
    "Satisfying Reverse Sponge Slice #shorts #oddlysatisfying",
    "1.5K views"
  ],
  [
    "https://www.youtube.com/shorts/sZoPqQ-fi4U",
    "Mesmerizing Floam ASMR #satisfyingvideos #satisfyingasmr",
    "1.9K views"
  ],
  [
    "https://www.youtube.com/shorts/CBuiIvhhmug",
    "Oddly Satisfying Foot Squish #oddlysatisfying #asmr",
    "1.6K views"
  ],
  [
    "https://www.youtube.com/shorts/Ir4fmGJwoLM",
    "Epic Foam Balloon Squish",
    "1.3K views"
  ],
  [
    "https://www.youtube.com/shorts/B-wK8-r32fQ",
    "Super Satisfying Soap Carve",
    "6.1K views"
  ],
  [
    "https://www.youtube.com/shorts/VLbPeipkxrc",
    "Blue Chalk Bird ASMR #shorts #satisfyingvideos",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/X_TU8JBDj0I",
    "Shaving Cream Juice Press #satisfyingvideos #sosatisfying",
    "2.9K views"
  ],
  [
    "https://www.youtube.com/shorts/U-sk5tbAmP8",
    "Foam Press PinkPantheress ASMR #asmr #sosatisfying",
    "7.3K views"
  ],
  [
    "https://www.youtube.com/shorts/B1upBW0VwuI",
    "Epic Marshmallow Squish #sosatisfying #satisfyingvideos",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/lIjAnvGvw9k",
    "Red Slipper Foam Squish #satisfyingvideos #oddlysatisfying",
    "6.4K views"
  ],
  [
    "https://www.youtube.com/shorts/ejDwOQgJ4hc",
    "Slime Stretches over Spikes #oddlysatisfying #satisfyingvideos",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/MOUhKDhsXUE",
    "Epic Silver Balloon Pop #oddlysatisfying #sosatisfying",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/EtGAVy5FLHM",
    "Reverse Paint Squeegee #satisfyingvideos #art",
    "4.7K views"
  ],
  [
    "https://www.youtube.com/shorts/3NS5pAwQQOI",
    "Satisfying Candle Carve #satisfying #sosatisfying",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/zPrt2TYNkE4",
    "Hot Knife Melts Rainbow Candle #sosatisfying #shorts",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/TDVTtMHMHbk",
    "Coke and Mentos Explosion #satisfying #shorts",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/-ZuGE2cgw84",
    "Up-Close Toothbrush Melt #satisfying #sosatisfying",
    "6K views"
  ],
  [
    "https://www.youtube.com/shorts/V3ODjAtWoAM",
    "Gray Foam Slicing #satisfying #sosatisfying #shorts",
    "1.7K views"
  ],
  [
    "https://www.youtube.com/shorts/Xrc4qsktiEM",
    "Exploding Foam Balloon",
    "2.8K views"
  ],
  [
    "https://www.youtube.com/shorts/W_aBwTAtHBs",
    "Carving Giant Cheese Block #satisfying #sosatisfying",
    "6.5K views"
  ],
  [
    "https://www.youtube.com/shorts/4g89vXRTnF0",
    "Yellow Yarn Slice",
    "5.7K views"
  ],
  [
    "https://www.youtube.com/shorts/Od1ietyGCKU",
    "Shaving Cream Shoe Squish",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/vxOa1bBvQBg",
    "Epic Pimple Popping",
    "3.2K views"
  ],
  [
    "https://www.youtube.com/shorts/Ovwcx-G5-CQ",
    "Gray Foam Slicing",
    "1.4K views"
  ],
  [
    "https://www.youtube.com/shorts/EBfCV7AvTkU",
    "Silver Sock Foam Squeeze",
    "6.7K views"
  ],
  [
    "https://www.youtube.com/shorts/dxa0U8lK-1g",
    "Paint Palette Scoop",
    "2.7K views"
  ],
  ["https://www.youtube.com/shorts/xhWEG3FN8_k", "Nutella Ooze", "2.1K views"],
  [
    "https://www.youtube.com/shorts/E6NwTq6jtFI",
    "Rainbow Crayon Peel ASMR",
    "1.7K views"
  ],
  [
    "https://www.youtube.com/shorts/gYZrEh4uWrg",
    "Slicing Blue Orange",
    "3.8K views"
  ],
  [
    "https://www.youtube.com/shorts/s6sZKnE4Qgk",
    "Melting Purple Pool Noodle",
    "2.5K views"
  ],
  [
    "https://www.youtube.com/shorts/9njWrnURvts",
    "| So Satisfying",
    "3.9K views"
  ],
  [
    "https://www.youtube.com/shorts/mI0xoaRyAr0",
    "Green Sand Squish",
    "3.1K views"
  ],
  [
    "https://www.youtube.com/shorts/T5-LRsi9MbE",
    "ASMR Tape Peel",
    "2.4K views"
  ],
  [
    "https://www.youtube.com/shorts/21gSiavZQFI",
    "Satisfying Foam Squish",
    "2.4K views"
  ],
  [
    "https://www.youtube.com/shorts/rX8sRFDJ8Hk",
    "Mirrored Ball Peanut Butter Squish",
    "3K views"
  ],
  [
    "https://www.youtube.com/shorts/eiF9wyhjdYA",
    "Plucking Whiteheads and Blackheads From Nose",
    "5.6K views"
  ],
  [
    "https://www.youtube.com/shorts/bYqS16d-Wr0",
    "Claw Ring Makeup Scrape",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/rCvEYojdexE",
    "Rainbow Slice Balloon Squeeze",
    "3.2K views"
  ],
  [
    "https://www.youtube.com/shorts/OEIQoreCLLs",
    "Pink Slime Pull From Noodle",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/bcf42rquQGo",
    "Golden Dripping Honey Up Close",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/f-WgQk9BGH0",
    "Mesmerizing Cube Foam Squish",
    "2.3K views"
  ],
  [
    "https://www.youtube.com/shorts/_XeECXv3uIg",
    "Oozing Purple Slime Pull",
    "4.8K views"
  ],
  [
    "https://www.youtube.com/shorts/oG-thAOCHLc",
    "Green Sock Foam Squish",
    "8.4K views"
  ],
  [
    "https://www.youtube.com/shorts/qlUCDNGB0mk",
    "Mesmerizing Purple Soap Carve",
    "7.2K views"
  ],
  [
    "https://www.youtube.com/shorts/mAh6Qd-hDv8",
    "Green Slime Satisfying Squeeze",
    "17K views"
  ],
  [
    "https://www.youtube.com/shorts/hB4kWPPrmmc",
    "Pulling Pink Slime From Croc",
    "3.4K views"
  ],
  [
    "https://www.youtube.com/shorts/Q3HjyGpRxqU",
    "Hot Knife Slices Cheesy Candle In Half",
    "12K views"
  ],
  [
    "https://www.youtube.com/shorts/y_DrxOkkwP8",
    "Honeycomb Satisfying Slime Scrape",
    "18K views"
  ],
  [
    "https://www.youtube.com/shorts/VLxoeZcZ5fA",
    "Perfect Pink Soap Carve ASMR",
    "87K views"
  ],
  [
    "https://www.youtube.com/shorts/n3nYde3kltA",
    "Burning Styrofoam With Hot Tool",
    "6.6K views"
  ],
  [
    "https://www.youtube.com/shorts/4NzIV5FbSjE",
    "Rainbow Clay Squeeze",
    "2.7K views"
  ],
  [
    "https://www.youtube.com/shorts/KXxrZ9yI1dM",
    "Slime Cheese Grater Pull ASMR",
    "8K views"
  ],
  [
    "https://www.youtube.com/shorts/FVqVRC4jp3k",
    "Cheese Grater Satisfying Reverse",
    "3.2K views"
  ],
  [
    "https://www.youtube.com/shorts/NuHqYKIODWQ",
    "Candle Melted With Torch",
    "2.1K views"
  ],
  [
    "https://www.youtube.com/shorts/Q10-viQPKOk",
    "Pimple Popping With Giant Screw",
    "9.7K views"
  ],
  [
    "https://www.youtube.com/shorts/8CNr0YOuptY",
    "Foamy Shoe Squish ASMR",
    "10K views"
  ],
  [
    "https://www.youtube.com/shorts/EdtAFZm3yR4",
    "Shaving Cream Satisfying Squish",
    "38K views"
  ],
  [
    "https://www.youtube.com/shorts/1FU4yztJSdY",
    "Rainbow Colored Sand Pour ASMR",
    "7.6K views"
  ],
  [
    "https://www.youtube.com/shorts/7s1wXoM30Eg",
    "Shaving Cream Mirror Squeegee",
    "7.3K views"
  ],
  [
    "https://www.youtube.com/shorts/6xStuW4Cgdw",
    "Flower Lipstick Rainbow Scissor Chop",
    "5.5K views"
  ],
  [
    "https://www.youtube.com/shorts/2sy1tCm0tHc",
    "Ultra Satisfying Green Sand Squeeze",
    "7.2K views"
  ],
  [
    "https://www.youtube.com/shorts/8AMmF8XA38k",
    "White Shaving Cream Ooze",
    "58K views"
  ]


]
#fmt: on

OUT_DIR = "./workspace/bg-vids"


def download_video_one(url, ydl):
    if not os.path.exists(f"{OUT_DIR}/{url.split('/')[-1]}.mp4"):
        ydl.download([url])
    #     console.log(f"[medium_purple3]downloaded {url}")
    # else:
    #     console.log(f"[green]exists: {url}")


def download_threaded(urls, ydl, adv, n_threads=6):
    q = Queue()

    def worker():
        while True:
            url = q.get()
            try:
                download_video_one(url, ydl)
                adv()
            finally:
                q.task_done()

    for i in range(n_threads):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    for url in urls:
        q.put(url[0])

    q.join()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestvideo[ext=mp4]',
        'outtmpl': f"{OUT_DIR}/random-%(id)s.%(ext)s",
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        'noprogress': True,
    })

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("Downloading videos", total=len(videos))

        # for url, title in videos:
        #     if not os.path.exists(f"{AUDIO_DIR}/{url.split('/')[-1]}.wav"):
        #         ydl.download([url])
        #         ffmpeg_cmd = f"ffmpeg -i {TEMP_DIR}/{url.split('/')[-1]}.webm -ac 1 -ar 16000 {AUDIO_DIR}/{url.split('/')[-1]}.wav"
        #         output = subprocess.run(
        #             ffmpeg_cmd.split(" "), capture_output=True)
        #         assert output.returncode == 0, f"ffmpeg failed: {output.stderr}"
        #         os.remove(f"{TEMP_DIR}/{url.split('/')[-1]}.webm")
        #     progress.advance(task)
        def adv():
            progress.advance(task)
        download_threaded(videos, ydl, adv)


if __name__ == "__main__":
    main()
