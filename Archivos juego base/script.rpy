# The script of the game goes in this file.

# Characters
define s = Character("Syira")
define h = Character("Huimin")
define d = Character("David")

#Images: Sprites
image syira n ="sprites/syira/syira-neutral.png"
image syira anger ="sprites/syira/syira-anger.png"
image syira frown ="sprites/syira/syira-frown.png"
image syira lookaway ="sprites/syira/syira-lookaway.png"
image syira relief ="sprites/syira/syira-relief.png"
image syira shock ="sprites/syira/syira-shock.png"
image syira closeeyes ="sprites/syira/syira-closeeyes.png"

image huimin 1n ="sprites/huimin/huimin-1-neutral.png"
image huimin 1crying ="sprites/huimin/huimin-1-crying.png"
image huimin 1dazed ="sprites/huimin/huimin-1-dazed.png"
image huimin 1frown ="sprites/huimin/huimin-1-frown.png"
image huimin 1lookaway ="sprites/huimin/huimin-1-lookaway.png"
image huimin 1relief ="sprites/huimin/huimin-1-relief.png"
image huimin 1shock ="sprites/huimin/huimin-1-shock.png"

image huimin 2n ="sprites/huimin/huimin-2-neutral.png"
image huimin 2crying ="sprites/huimin/huimin-2-crying.png"
image huimin 2dazed ="sprites/huimin/huimin-2-dazed.png"
image huimin 2frown ="sprites/huimin/huimin-2-frown.png"
image huimin 2lookaway ="sprites/huimin/huimin-2-lookaway.png"
image huimin 2relief ="sprites/huimin/huimin-2-relief.png"
image huimin 2shock ="sprites/huimin/huimin-2-shock.png"
image huimin 2closeeyes ="sprites/huimin/huimin-2-closeeyes.png"

#Images: Backgrounds
image bathroom ="background/bathroom.jpg"
image chaletback ="background/chalet-back.jpg"
image chaletliving ="background/chalet-living.jpg"
image chaletliving2 ="background/chalet-living-glass.jpg"
image chaletliving3 ="background/chalet-living-him.jpg"
image chaletlivingdream ="background/chalet-living-dream.jpg"
image chaletoutside ="background/chalet-outside.jpg"
image chaletroomdark ="background/chalet-room-dark.jpg"
image chaletroomlight ="background/chalet-room-light.jpg"
image forest ="background/forest.jpg"
image syiraroomdark1 ="background/syira-bedroom-dark1.jpg"
image syiraroomdark2 ="background/syira-bedroom-dark2.jpg"
image syiraroomlight ="background/syira-bedroom-light.jpg"

#Images: CGs
image forestcg1 ="cg/forest-cg-1.png"
image forestcg2 ="cg/forest-cg-2.png"
image forestcg3 ="cg/forest-cg-3.png"
image forestcg4 ="cg/forest-cg-4.png"

image phonecgcall ="cg/phone-cg-call.png"
image phonecgig ="cg/phone-cg-ig.png"

image showercg ="cg/shower-cg.png"

image huimincg1 ="cg/huimin-cg-1.jpg"
image huimincg2 ="cg/huimin-cg-2.jpg"
image huimincg3 ="cg/huimin-cg-3.jpg"
image bedroomcg1a ="cg/bedroom-cg-1-a.png"
image bedroomcg1b ="cg/bedroom-cg-1-b.png"
image bedroomcg1c ="cg/bedroom-cg-1-c.png"
image bedroomcg1d ="cg/bedroom-cg-1-d.png"
image bedroomcg1f ="cg/bedroom-cg-1-f.png"
image bedroomcg1e ="cg/bedroom-cg-1-e.png"
image bedroomcg1g ="cg/bedroom-cg-1-g.png"
image bedroomcg1h ="cg/bedroom-cg-1-h.png"
image bedroomcg2a ="cg/bedroom-cg-2a.png"
image bedroomcg2b ="cg/bedroom-cg-2b.png"

image fightcg1 ="cg/fight-cg-1.png"
image fightcg2 ="cg/fight-cg-2.png"
image fightcg3 ="cg/fight-cg-3.png"

image shadow1 = "cg/shadow-1.png"
image shadowfull = "cg/shadow-4.png"

image endinglovecg1 ="cg/endinglove-cg-1.png"
image endinglovecg2 ="cg/endinglove-cg-2.png"
image endinglovecg3 ="cg/endinglove-cg-3.png"
image endinglovecgfull ="cg/endinglove-cg-full.jpg"

image endingviolencecg1 ="cg/endingviolence-cg-1.png"
image endingviolencecg2 ="cg/endingviolence-cg-2.png"
image endingviolencecg4 ="cg/endingviolence-cg-4.png"
image endingviolencecgfull ="cg/endingviolence-cg-full.jpg"

image splash = "splash.jpg"
image warning = "warning.jpg"

image black = "#000000"
image white = "#FFFFFF"

#Position
init:
    $ cleft = Position(xpos=0.25, ypos=1.0)
    $ cright = Position(xpos=0.75, ypos=1.0)
    $ cgcenter = Position(xpos=0.5, ypos=0.65)
    $ cgphone = Position(xpos=0.5, ypos=0.72)

#CG Gallery

init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    g.locked_button = "gallery_locked.png"

    g.button("forest")
    g.condition("persistent.unlock_forest")
    g.image("gallery/forest-cg-1-full.jpg")
    g.image("gallery/forest-cg-2-full.jpg")
    g.image("gallery/forest-cg-3-full.jpg")
    g.image("gallery/forest-cg-4-full.jpg")

    g.button("huimin")
    g.condition("persistent.unlock_huimin")
    g.image("gallery/huimin-cg-1.jpg")
    g.image("gallery/huimin-cg-3.jpg")

    g.button("bedroom")
    g.condition("persistent.unlock_bedroom")
    g.image("gallery/bedroom-cg-1-full.jpg")
    g.image("gallery/bedroom-cg-2-full.jpg")

    g.button("fight")
    g.condition("persistent.unlock_fight")
    g.image("gallery/fight-cg-1-full.jpg")
    g.image("gallery/fight-cg-2-full.jpg")
    g.image("gallery/fight-cg-3-full.jpg")

    g.button("endlove")
    g.condition("persistent.unlock_endlove")
    g.image("gallery/endlove-cg-1-full.jpg")
    g.image("gallery/endlove-cg-2-full.jpg")
    g.image("gallery/endlove-cg-3-full.jpg")
    g.image("gallery/endinglove-cg-full.jpg")

    g.button("endenvy")
    g.condition("persistent.unlock_endenvy")
    g.image("gallery/endenvy-cg-1-full.jpg")
    g.image("gallery/endenvy-cg-2-full.jpg")
    g.image("gallery/endenvy-cg-3-full.jpg")
    g.image("gallery/endingenvy-cg-full.jpg")



    #Step 3: generate the gallery and how it looks
screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    use game_menu(_("Gallery"), scroll="None"):
    # A grid of buttons.

        fixed:

            grid 3 2:

                xalign 0.5
                yalign 0.4

                spacing 0.05

                add g.make_button("forest", "gallery/unlock_forest.png", xalign=0.5, yalign=0.5)
                add g.make_button("huimin", "gallery/unlock_huimin.png", xalign=0.5, yalign=0.5)
                add g.make_button("bedroom", "gallery/unlock_bedroom.png", xalign=0.5, yalign=0.5)
                add g.make_button("fight", "gallery/unlock_fight.png", xalign=0.5, yalign=0.5)
                add g.make_button("endlove", "gallery/unlock_endlove.png", xalign=0.5, yalign=0.5)
                add g.make_button("endenvy", "gallery/unlock_endenvy.png", xalign=0.5, yalign=0.5)



define persistent.unlock_forest = False
define persistent.unlock_fight = False
define persistent.unlock_bedroom = False
define persistent.unlock_huimin = False
define persistent.unlock_endenvy = False
define persistent.unlock_endlove = False

default love = 0

#SPLASH

label splashscreen:
    scene black with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(0.5)

    return
    with dissolve

# GAMESTART

label start:
    
    $ quick_menu = False
    stop music fadeout 1.0
    scene black with dissolve
    with Pause(1)
    show warning with dissolve
    pause
    scene black with dissolve
    with Pause(0.5)
    $ quick_menu = True

    play music "audio/bleak-v1.wav"
    scene forest with dissolve
    play sound "audio/crickets.mp3"

    "The night was sweltering, warm with a heavy humidity that sank into my clothes. {w}I feared that reaching to put on our shoes would wake someone, so we snuck out of the camp barefoot."

    show forestcg1 at cgcenter
    with dissolve
    play sound "forest-walk.mp3"

    "But I barely noticed the earth caked between my toes — instead I was focused on her hand, warm where it was wrapped around my own."    
    "I let her lead me along to the forest at the edge of the campsite."

    hide forestcg1
    with dissolve

    h "Syira, do you have the string?"
    "I blinked, then felt around in my pocket for the spool of red thread. I had taken it from my home economics kit before we left for the trip, along with a small pair of scissors."
    s "Yea."

    "We had first discovered the ritual on a blog. There had been many, ranging from confusing to downright morbid. But when we landed on this one, it felt safe enough to try. After all, we just had to–"

    show forestcg2 at cgcenter
    with dissolve
    play sound "audio/clothing2.mp3"
    "Tie a red string to a banana tree."

    show forestcg3 at cgcenter
    with dissolve

    "Connect that same string to our pinkies."

    show forestcg4 at cgcenter
    with dissolve

    "And make our wish."
    h "Remember, we have to make the same wish or it won’t come true."
    s "Yea, I know."
    h "Best friends forever."

    hide forestcg2 with dissolve
    hide forestcg3 with dissolve
    hide forestcg4 with dissolve

    "I nodded to show her that I had understood. Huimin returned a smile, gentle and sincere. Even in the dark where I could barely make out her features, the gesture made my chest tight."
    "Then, we both lowered our heads and clasped our hands together again."
    "{i}Make the wish in your heart{/i} — the blog had instructed. My heart thundered in my chest. {w}Huimin wished for us to stay best friends forever."
    "And I—"
    "I wished for her to be mine."
    $ persistent.unlock_forest = True
    stop music fadeout 1.0


label syiraroom:

    scene black with dissolve
    "Whatever demon or spirit that was supposed to grant our wish never did."
    scene syiraroomlight with dissolve
    play music "audio/Pyrrhic.wav" fadein 3.0
    "More than a decade later, Huimin and I are neither together nor best friends. At least, best friends probably see each other more in-person than on Instagram."

    show phonecgig at cgphone
    with dissolve

    "Instead, she’s been seeing this guy for five years. Their smiling faces pressed together along with the caption teases me: {i}anniversary chalet with the bae!{/i}"
    "I can already see how it will all go from here. Soon, they’ll get engaged. Then they’ll apply for a BTO flat, get married, and move out together."
    "It’s the ever popular Singaporean dream of building a nuclear family."
    "Huimin had always wanted her own place, so I should be happy for her. But bitterness churns in my stomach."
    "Her boyfriend's smile taunts me, reminding me of what I can't have with her in this stupid, heteronormative country."

    hide phonecgig with dissolve

    "I close the app."

    scene syiraroomdark1 with dissolve

    "Years ago, despite everything, I thought we had a chance. I thought that if life just meandered and turned in the right way, if we were stubborn enough and lived on our own rules, we could have our happy ending too."
    "Now I don’t know anymore."
    "I think of that ritual. If it had worked, would it have saved or doomed me?"
    "A tired sigh consumes me and I close my eyes. It’s too much for tonight. I don’t want to spiral into this again."
    stop music fadeout 1.0
    scene black with fade
    play music "audio/Hidden-Path.mp3"
    "I am indoors but there is sand beneath my feet. It must have followed me from the beach, stubborn even as I walked for miles, clinging to my soles to finally make it into my home."
    "But this is not my home. I am in someone else's house."

    scene chaletlivingdream with fade
    play sound "audio/horror-ringing-short.mp3"
    "There is a stench in the air."
    "The smell of a mess that had not been cleaned up, of something left out to rot."
    "Something resembling..."
    play sound "audio/jumpscare.mp3"
    show shadowfull
    "—!!{w=0.5}{nw}"
    scene black with fade

    scene syiraroomdark1 with vpunch
    play sound "audio/phone-ringing.mp3"
    "It was a dream. As I shake off the grogginess, I realise my phone is ringing.{w} It must be the middle of the night. I frown — calls this late are never good."

    show phonecgcall at cgphone 
    with dissolve

    "Huimin? Why would she…call {i}me?{/i}"
    "Despite the oddity of the call, my heart swells with fondness at the thought of her on the other side. Without sparing another moment, I accept the call."

    h "Syira? Syira are you there?"
    "She sounds frantic, her voice breathless and pitched."
    s "I'm here. Huimin, I'm here. What's wrong?"
    h "Oh my god, Syira I–"
    "The line cracks, movement muffling the receiver. As I strain to hear her, I realise in horror that Huimin is crying."
    s "Calm down, tell me what happened."
    h "D-David and I had a fight and– I pushed him by accident and then he just…"
    s "He just…?"
    h "Can you come to the chalet, please? I don't know what to do!"
    s "Okay, can you text me the address? I'll go now."
    h "Yes…yes, I'll text you. You'll help me, right?"
    s "Of course, we're best friends."
    "I don't know why I said that. We haven't even acknowledged that in years."
    h "Thanks, Syira."

    hide phonecgcall with dissolve

    "After the call ends, I stare at the screen, letting it sink in."
    "Something had happened between Huimin and her boyfriend.{w} Something bad.{w} My first thought was that he had hurt her. But {i}she{/i} said she had pushed {i}him.{/i}"
    "A dark, malicious thought began to take root in my head.{w} Are things finally turning in my favour? Did the demon coiled in the trunk of that banana tree hear my wish after all?"
    "My phone pings, startling me out of my thoughts."
    "A few texts had come in from Huimin. The first one was a badly typed address, followed by another text that corrects a few typos while also making new ones. Finally, a third one comes in with everything laid out, corrected."
    "{i}This one.{/i} She says. {i}Sorry.{/i}"
    "I fire a quick text back to acknowledge it, then move to get changed to leave the house. At this hour, the buses and trains have long stopped running."
    "A cab is too expensive. I grab my bicycle instead."
    stop music fadeout 1.0

label chalet:

    scene black with dissolve
    play music "audio/Bleak-v1.wav"
    "I know the chalet is about twenty minutes away by bike. It's an old establishment on East Coast park, popular for barbecues near the beach."
    "I've been there many years ago, as part of our secondary school class gathering. It was supposed to be a fun sleepover with everyone — which in theory was exciting, but became a huge mess in execution."
    "Eventually, Huimin snuck over to my house and slept over there instead. I hated the class trip, but our own sleepover felt special. That was when we–"

    scene chaletoutside with dissolve

    "I stop my thoughts there.{w} I've arrived at Huimin’s chalet. It's dark, but I can make out the villa number beside the door. It's one of the last few villas at the edge of the property, closer to the forest than the beach."

    "I leave my bicycle by the side of the road and walk up to the door. I knock three times."
    play sound "audio/knocking.mp3"
    show syira n at cleft
    with dissolve
    s "Huimin? It's me, Syira."
    show huimin 1frown at cright
    with dissolve
    show syira shock
    "The door unlocks and Huimin peers out. I'm taken aback by the blood soaked into her clothes."
    s "H-Huimin?"
    show huimin 1shock
    h "Syira!"
    "She reaches for my arm, grabbing on tightly. Her nails dig into my flesh as she trembles violently."
    h "I can trust you right? Promise me you won't call the police. Promise me, please!"
    "The words tumble out of her, a desperate and incoherent plea. My mind is whirring."
    show syira frown
    s "Are…you hurt?"
    h "Huh?"
    "I reach out with my other hand, pushing back her unkempt hair to look at her face properly. It seems like there's blood everywhere, even splattered on her face. It makes me sick, thinking any of it could be hers."
    s "The blood. Did you get hurt?"
    "Huimin finally realises what I'm asking about. She peers down at her shirt, seeming to take in her own appearance with fresh shock."
    h "I…it's not mine."
    show syira relief
    s "Okay."
    "I breathe a sigh of relief."
    show huimin 1crying
    show syira frown
    h "But Syira, I did something bad. Please don't call the police yet, okay? I didn't mean it! I really didn't mean it!"
    h "You'll help me, right?"
    "Her tear-stained face tugs at my heart. Whatever conscience I had crumbles easily in the sway of her plea. I have a slow, sinking realisation — like an anchor doomed for the ocean floor — {w}that I was ready to do whatever she asked of me."
    show syira relief
    s "Of course. I'll help you."
    show huimin 1relief
    "A small relief blooms on her face, but quickly disappears as she leads me into the villa."
    stop music
    scene chaletliving3 with vpunch
    play music "audio/Ritual.mp3"
    h "He's…here."
    "Huimin pauses in the doorway leading to the living area. It's the scene from my dream, but crystal clear and real."
    "The room is in disarray, furniture upturned and thrown from its original place — the remnants of a fight. David has collapsed head-first into a glass table, shards exploded and littered over the floor with blood pooling under his body."
    "Did Huimin do this?"
    "Beside me, a loud gasp escapes her."
    show huimin 1shock at cright
    with hpunch
    h "Oh my god…oh my god…"
    h "S-Syira, did I k-kill him?"
    show syira frown at cleft
    with moveinleft
    "I hold my breath, heart hammering in my chest as I approach the man. The glass crunches under my shoes and blood sticks to the soles. This close, the blood stuck in his hair and skin is dark and viscous, something vile and utterly wrong."
    "I knew the answer before I pressed two fingers to his neck — that there would be no pulse."
    s "He's dead."
    play sound "audio/screaming.mp3"
    hide huimin with moveoutbottom
    "Huimin screams, chest heaving like an animalistic reaction."
    "I whirl around, pushing her hair back to look at her face. She looked pathetic, pale and trembling as she all but fell apart."
    show huimin 1crying at cright
    with moveinbottom
    s "Huimin, look at me."
    show syira frown at center
    with move
    s "I promised that I'll help you, right?"
    "She nods slowly."
    s "So I'll help you. Let's bury him. And then clean up."
    show huimin 1frown
    h "Okay."
    
    scene black with dissolve
    "I tug on Huimin's arm, helping her up to her feet. She pointedly avoids looking at David again, rifling through a few drawers before pulling out large black trash bags. I let her handle his feet while I dealt with his bloodied head."
    "Together, we wrapped the body in layers and layers of black plastic, until we could see neither his skin or the clothes on his back."

    scene chaletback with dissolve
    "We drag the body out to the back. The chalet sits on the edge of the property, facing out into a forest. Grass had overgrown in neglect, long and spindly at our feet."
    s "Let’s bury him here."
    play sound "audio/digging.mp3"
    "I dug my hand into the earth, prying grass and soil away. It’s long, arduous work, toiling away with nothing but our bare bodies."
    "Maybe we should have scoured for tools in the house — something to use as a shovel. But as I peer over at Huimin, the bare motion seems to feel like repentance."
    play sound "audio/digging.mp3"
    "I don’t speak a word to her. I just keep digging, nails growing black with dirt and skin turning bloodied. {w}We paid, together."
    "When at last a large enough hole appeared, we pushed the body in and covered it up."

    scene chaletliving2 with dissolve
    "The room also needed cleaning up."
    "Huimin gathers a broom to sweep up the glass shards that had flown to every corner of the room upon impact. I scrub blood off the tiles, turning an old rag pink."
    
    scene chaletliving with dissolve
    show syira n at cleft
    show huimin 1n at cright
    with dissolve
    s "I think…we're done."
    stop music fadeout 5.0
    "Huimin stares at me wordlessly, eyes blinking in a daze. I realise her blouse is still soaked with blood, the substance caking into her hair along with dirt from the backyard. Her face is blotchy with dried tears, sweat pooling at her neck."
    s "You should take a shower."
    "Huimin reaches out, fingers closing around my jacket."
    h "You too."

label bathroom:

    scene bathroom with dissolve
    play music "audio/Pyrrhic.wav" fadein 3.0
    "I wasn't sure what she meant, or what was going to happen. I wasn't sure, up till we were shuffling into the bathroom together, shedding our clothes and stepping into the shower stall where the hot water poured down both our backs."
    "{i}You can go first.{/i} The phrase lingers at the tip of my tongue, always on the verge of being voiced, before I swallow it down."
    "Something about the way Huimin had closed her fist over the lapel of my jacket.{w} The way she tugged on my arm to lead me into the bathroom.{w} The way she loosened my hair tie and pulled my ponytail apart."
    "I couldn't say it. Instead, I grasped at the straws presented to me, fingers threading through her fine black hair."
    show showercg at cgcenter
    with dissolve
    play sound "audio/shower.mp3"
    s "I'll help you wash your hair."
    h "Okay."
    "As the soap ran down her back, I noticed purplish bruises blooming on her back. They were stark against her fair skin, big patches that seemed deliberate rather than accidental."
    "Though, as Huimin shivered, I wondered if she would want to talk about it at all."

    menu:
        "Ask her about the bruises":
            jump her_father
        "Talk about a memory":
            $ love += 1
            jump primary_four

label her_father:

    s "Huimin…are you okay? Your back is covered in bruises."
    h "Oh."
    "I try to be careful, stringing my words together cautiously so she doesn't close off."
    s "Is it recent?"
    h "I don't know. I can't really keep track."
    h "My dad gets angry all the time. It was probably something stupid like letting my wet hair drip on the floor or forgetting to arrange the plates a certain way. Who knows."
    "I bite my lip. Huimin has a violent father."
    "As the eldest daughter in the family, she’s been raised to shoulder the responsibilities of taking care of both the household chores and her younger brother. She's the most hardworking and meticulous person I know, yet her father continues to find fault in her."
    s "I'm sorry."
    h "…It's not your fault. I'm just unlucky."
    h "Sometimes I wonder if I did something to deserve this. If I'm a bad daughter after all."
    s "Huimin, you're not…"
    h "Then what am I supposed to do for my family to be happy with me? It feels like there's an imaginary bar I'm trying to reach, but I don't know where or what it is."
    h "It's just incomprehensible to me."
    h "And now David…I don't even know how it happened. It was as if something took over me and I just…{w} Oh god, am I just like my dad? Just as violent and senseless–"
    s "That's not true, Huimin. It was an accident. I know it is. You didn't want to hurt him."
    h "…Yea. I won't hurt David on purpose, right?"
    h "After all, I love him. I…"
    h "I wanted to marry him."
    s "Oh."
    "My heart sinks.{w} I've known this, but still my gut wrenches with disappointment."
    h "If I could marry him, we could get a house and I could move out."
    h "It felt like the only way I could escape. The only way my family would let me go."
    h "But now it's over. My dream is over, Syira."
    stop music fadeout 3.0
    jump chalet_back

label primary_four:

    s "Do you remember when we were in Primary four together?"
    s "I got bullied and you had to wash my hair for me, just like this."
    h "Oh…yea. You were much more timid then."
    s "And you were unhinged."
    "Huimin lets out a soft, humourless laugh."
    h "Yea. Things were so different back then."
    s "I remember I got called to read aloud in class. Back then, I had a hard time projecting my voice. Even something simple like reading a passage aloud in class was a nightmare."
    h "The teacher was such a jerk for picking on you for that."
    s "Yea, she made me repeat it again and again because I wasn’t loud enough, until the class got frustrated with me."
    h "It was a bunch of boys who picked on you after, right?"
    s "They were pissed that we were late to recess break."
    "The boys cornered me after class ended, confronting me as if I had done the whole thing on purpose. Caught off guard, I didn’t know how to respond as my cheeks burned in mortification."
    "It all happened so fast. Suddenly, someone was grabbing my hair and another was uncapping a bottle of glue and pouring it onto my braids."
    s "You appeared right then and saved me."
    h "More like just cursed them out until they ran off."
    s "Hah, yea. What did you use? Dialect?"
    h "Yeap. Learnt it from my dad."
    "I was grateful to Huimin, clutching onto her hand like a lifeline as she led me to the washroom to clean up. Shame had consumed me and I apologised profusely, but she deflected all of it."
    "She forced me to accept her care instead."
    "Huimin guided me to tilt my head back into the sink, tugging off my hair tie to release the black waves of my hair. Then she switched on the tap and ran the water through my hair."
    "I closed my eyes, sinking into the sensations."
    "Her fingers combed through my hair, starting at the tips, carefully breaking up clumps of dried glue. She worked her way up to my scalp, tugging and untangling the strands of my hair."
    "She was so meticulous, so gentle, that my heart ached. It was such a sharp contrast to how she treated the boys. I couldn’t help thinking how lucky I was to be the one best friend that she had chosen."
    "It was the first time I felt painfully vulnerable in her presence. For someone like me, who doubted everything and struggled to keep my head up, her unwavering presence was so precious."
    s "I’m glad we became friends."
    h "Me too."
    "Huimin seems calmer.{w} Her shoulders have loosened up and her eyes are closing. Running water fills the silence."
    "I wonder if she ever gets the same fluttering, vulnerable sensation I did.{w} If this feels as intimate for her as it did for me back then, or if it's really nothing but a favour."
    h "Thank you, Syira."
    s "It's nothing. I think your hair is clean now."
    h "No, I mean…talking about the past. It was nice."
    h "I missed it."
    stop music fadeout 3.0
    jump chalet_back

label chalet_back:

    scene chaletback with fade
    play music "audio/bleak-v1.wav" fadein 3.0
    "I leave Huimin to settle down in the room. Something draws me to the backyard again."
    "The grave we’ve made is still there, a fresh mound of dirt in the midst of long, overgrown grass."
    "I think of his body, broken and buried beneath.{w} I want him to rot.{w} I want his flesh and skin to break apart and separate from bone, for the earth to consume him whole and leave nothing to touch her ever again."
    play sound "audio/foliage.mp3"
    "My head whips up at a sound, squinting at the trees."
    "Belatedly, I’m reminded of the ritual Huimin and I had done as kids. How we had tied a red string to a tree just like one of many here."
    show shadow1 with hpunch
    play sound "audio/horror-ringing-short.mp3"
    s "—!!"
    s "Who is—"
    hide shadow1
    "Before I can get my sentence out, the figure disappears as suddenly as it had appeared."
    "I’m left with my heart pounding like a drumbeat, limbs trembling and skin speckled with goosebumps. I quickly return to the room."
    stop music fadeout 1.0

label chalet_bedroom:

    scene chaletroomlight with dissolve
    play music "audio/Threnody.wav" fadein 3.0
    "Huimin had changed into a fresh set of clothes, but hadn’t moved to dry off her hair. She stood motionless in a corner of the room, wet hair dripping onto the floor."
    "I grab a towel and approach her."
    show syira n at cleft
    with dissolve
    s "Huimin."
    show huimin 2dazed at cright
    with dissolve
    "Huimin turns at the sound of my voice. She had stopped crying, but her eyes still looked glassy, eyes red-rimmed and puffy.{w} Despite looking in my direction, I wasn’t sure if she was seeing me."
    "I ignore that and push on."
    s "Come here, I’ll help you dry off your hair."
    play sound "audio/clothing1.mp3"
    "She doesn’t move. I go to her instead. She doesn’t protest when I take hold of her hair, sandwiching it between the towel and rubbing the strands dry."
    h "I’m sorry."
    show syira frown
    s "…It’s not your fault. You didn’t mean to."
    h "Did I really? …Did I really not mean to?"
    "I pause. {i}No, of course she didn’t.{/i} The guilt is just eating away at her.{w} I wish it would end already, be done flowing out of whatever well of conscience it came from.{w} I wish we could move on, away from the shadow of him."
    "He’s dead, for god’s sake."
    "I wish I had done it instead. I won’t look back."
    s "It was an accident. That’s all it was, Huimin."
    "Huimin falls silent again."

    menu:
        "Talk about how you graduated (together)":
            $ love += 1
            jump graduation
        "Talk about university (where she was dating him)":
            jump university
        

label graduation:
    show syira relief
    s "Do you remember when we graduated together?"
    h "…Secondary school?"
    s "Yea."
    show syira closeeyes
    "It was our first real taste of freedom — the first time in years I could spend months without worrying about either homework or exams. Both of us were sixteen, teenagers longing to eat out, play around and stay out late." 
    "We lusted for the autonomy that adulthood promised. I wanted to do everything all at once.{w} It was exhilarating, especially so with Huimin by my side."
    show syira relief
    s "Do you remember how we would split a McDonald’s meal so we could save money? Or how we would walk around a whole mall with bubble tea and just window shop?"
    s "We were so carefree back then…"
    show huimin 2closeeyes
    h "We were."
    show syira lookaway
    "Even though it was mundane in hindsight, those times meant a lot to me. It was what I clung onto after Huimin and I drifted apart."
    "Did she think back about them too?"
    show syira n
    s "Oh, that was when I dyed my hair for the first time. We finally didn’t have annoying school rules about our hair or attire, so I itched to do something with it."
    show huimin 2dazed
    s "I made you pick out the colour for me."
    "It’s the same maroon shade I have right now. When the colour first came out, Huimin said it was so pretty on me."
    "And I had kept it since then, religiously redyeing the roots each time they grew out until it felt as if it was my own hair."
    h "It’s still the same colour."
    show syira relief
    s "It grew on me."
    show syira closeeyes
    "God, going through our memories really feels like pressing on a bruise. A bruise shaped like a pathetic, fruitless crush."
    "Back then, things felt almost perfect. I thought our relationship was heading in the right trajectory, that it was only a matter of time and I could get the ending I wanted."
    "That she'll say yes instead of pushing me away."
    jump chalet_bedroomdark

label university:
    show syira n
    s "Do you remember what it was like in university?"
    show syira lookaway
    s "I was anxious. It was the first time we were really apart."
    s "I…had a hard time, actually. I was unsure about the new environment, so I tried to keep in touch with you as much as I could."
    show huimin 2closeeyes
    h "I see."
    "When university started, both of us had to adjust to a new kind of curriculum and new classmates. I was lost without her, frantically clinging onto our friendship through text messages and calls."
    show syira closeeyes
    "On the other hand, Huimin fit in better in her class. She made friends quickly —{w} she even met… him."
    show syira n
    s "University was where you met him, right?"
    show huimin 2dazed
    h "Yes, I met David then."
    show syira frown
    "David was her first proper boyfriend. She was devoted to him, almost desperately so. I hated it."
    "I remember jealousy coiling in my gut, thinking that — {i}it’s so easy for him.{/i}"
    "David was a tall and decent-looking boy pursuing business in university. He was popular and sociable in class, did well in school and even played sports on the weekend."
    "The exact type of guy who would make an ideal son-in-law."
    "I knew it wasn’t hard for him to approach Huimin. And it wasn’t hard for Huimin to say ‘yes’, either. Because boys liked girls, and girls liked boys, didn’t they?"
    "I could try to best him in everything. I could work to get better grades, play more sports, grow my social circles — {w}but my attempts for anything more than a platonic friendship will always be wrought with disappointment."
    "All I could do was step back and watch it unfold. Let envy claw at the hollow of my gut, hungry for what it can’t have."
    s "I…wanted to be happy for you. But he always wanted your meal times and weekends. You started giving so much of yourself to him.{w} I just felt…"
    s "Pushed aside, I guess."
    show huimin 2closeeyes
    h "I’m sorry."
    show syira lookaway
    s "It’s fine. It’s not all your fault."
    show syira closeeyes
    "I remember trying to hate her for treating our friendship like this.{w} But once I had the opportunity to see her again — a smile, a hug, the sound of her melodious voice — all that bitterness was pushed under the rug."
    show huimin 2dazed
    s "I just missed you."
    s "And I still do, now."
    "Sometimes I think — if only I was a boy. If only I was {i}him{/i}. Oh, how much simpler it would be."
    "I won’t even need a twisted wish like this. I won’t even need a demon like {i}Her.{/i}"
    "I think of David, the boy we had buried under layers and layers of earth. I think of the square edge of his boyish jaw, the bob of his adam’s apple, the broad slope of his shoulders."
    "Does Huimin still love those parts of him, rotting as he must be?"
    "My stomach feels so hollowed out from disappointment that it hurts."
    jump chalet_bedroomdark

label chalet_bedroomdark:

    show syira n
    show huimin 2closeeyes
    stop music fadeout 3.0
    h "Sorry, I'm tired. I'm going to lie down."
    hide huimin with dissolve
    h "Can you turn off the light?"
    s "…Okay."
    play music "audio/Hidden-Path.mp3" fadein 5.0

label decision:
    menu:
        "Turn off the light":
            play sound "audio/switch.mp3"
            jump lights_off
        "Wait":
            jump wait_lights

label wait_lights:
    show syira closeeyes
    "I hesitate, finger hovering over the switch."
    "The shadow lingers on my mind."
    h "Syira?"
    jump decision

label lights_off:
    scene chaletroomdark with hpunch
    show shadowfull
    play sound "audio/jumpscare.mp3"
    s "—!!"
    "I feel something squeezing my chest, making it impossible to breathe."
    "I think of whispered ghost stories and urban legends, of the secrets muttered between two teenage girls. I think of Huimin, and what happened when—"

    menu:
        "Huimin and her boyfriend fought":
            jump dream_fight
        "We slept over together":
            $ love += 1
            jump dream_sleepover

label dream_fight:
    stop music fadeout 1.0
    scene black with fade
    play music "audio/Forest.mp3"
    "She said they had a fight."
    scene chaletliving with fade
    "I see the room before me again, furniture in disarray and broken glass strewn over the floor. I can hear Huimin sniffling, holding back tears. David is gritting his teeth."
    show fightcg1 at cgcenter
    with dissolve
    h "I thought we wanted to get engaged because you loved me?"
    d "Babe, I do."
    h "Then why are you treating applying for a BTO flat together like a business transaction? It’s supposed to be our home, not an investment!"
    d "You’re being unreasonable. How can you ask me to pay more for the downpayment just because I earn a little more than you? It should be a 50/50 split. Otherwise, you’re just taking advantage of me."
    h "But David, you know I have almost no savings. I pay for my family’s bills and whatever expenses they suddenly throw at me. I’m not trying to take advantage of you, I’m just asking for your help."
    d "So you think I have no responsibilities? Or that I’m made of money just because I paid for our Bali trip last year?"
    h "No, no, I’m not saying that—"
    d "I treat you so well, but you’re just complacent now. Were you planning to use me to pay for a flat just so you can move out?"
    h "That’s not it…"
    d "If you wanted a house of your own so bad, you should have worked harder so you can afford the downpayment instead of relying on a guy."
    d "Girls are all like this. You say you have no money, but then you go shopping and spend it all on frivolous stuff."
    h "I-I didn’t…"
    d "Stop making excuses! I’m sick of you crying about everything! Do something instead of relying on me!!"
    hide fightcg1 with dissolve
    play sound "audio/impact.mp3"
    "Then, David grabs her."
    "No, no, {i}no.{/i}{w} Don’t hurt her!"
    "Huimin gasps, bruises blooming under his tight hold."
    h "No, David please—"
    play sound "audio/crash-small.mp3" 
    "He flings her into the furniture. Huimin cries out as she crashes and rolls onto the floor with a dull thud."
    show fightcg2 at cgcenter
    with dissolve
    d "Did you really love me? Or were you just using me?"
    h "David, I-I love you. I really do."
    "She’s on her hands and knees, reeling from the blow. David approaches her."
    d "Stop fucking lying."
    "He grabs Huimin again, jerking her head up to look at him. Betrayal burns in her eyes. She knows this violence too well."
    "Anger boils in my blood. How dare he do this to her?"
    "I want to reach into the memory, break his arms and bruise him. Even if all I have are my bare teeth and fingernails, I will tear up his skin and make him bleed."
    scene black with dissolve
    "My body grows hot, like a fire is rising in my gut. Darkness spots over my vision and something tugs at my limbs."
    "Her.{w} The spirit in the banana tree.{w} The demon I told my wish to."
    "Then, I am nails digging into his skin, scratches and blood trailing where I dream of revenge.{w} This is Huimin’s body, but she is a vessel for my wish. And I wish to hurt him, tear him up, ruin him."
    "David fights back, bruises and blood blooming where we crash into each other. Frustration bubbles up in my chest. It’s unfair how strong he is, it’s unfair how easily he can get his way, it’s unfair how he gets to be — him."
    "I stare at him, watching the blood trail down his face. It must mirror what he’d done to her."
    "{i}I want what you have.{/i} I start to say. {i}I don’t care how, anymore.{/i}"
    "I don’t know if he hears me. The words are in my head, screaming, but my mouth doesn’t move to form them."
    play sound "audio/hissing-soft.mp3"
    "Then, I hear Her, whispering."
    "{i}Take it. Kill him so you can take it.{/i}"
    "A new strength seeps into my arms, something so intense that it almost sends me reeling off balance. I step forward and shove him with all of it."
    scene chaletliving with hpunch
    show fightcg3 at cgcenter
    with hpunch
    play sound "audio/crash.mp3"
    "David crashes into the table. The top shatters, glass scattering over the floor. His body slumps into the side, blood pooling on the floor, a deep deep red."
    stop music fadeout 3.0
    "This is how it happened."
    $ persistent.unlock_fight = True
    jump after_dream


label dream_sleepover:
    stop music fadeout 1.0
    scene syiraroomdark2 with fade
    play music "audio/Threnody.wav"
    "I see my bedroom in its familiar layout. Things have been shuffled around, nostalgic trinkets scattered around the room again."
    show bedroomcg1a at cgcenter
    with dissolve
    "Huimin and I are teenagers, huddled on my bed refusing to go to sleep even though it was well past midnight. We had ditched the class gathering earlier in the day, cycling to my place nearby to hang out instead."
    h "What do you think they're doing now?"
    s "Probably playing truth or dare or some stupid games."
    show bedroomcg1b at cgcenter
    "Huimin lets out a huff."
    h "Yea, they'll probably try to pair me up with Weijie again if I was there."
    "My throat tightens. This was around the time in my life when I started to wonder if I liked girls."
    "It was a secret I was desperate to hide. The thought of anyone finding out, especially my parents, left me deeply mortified."
    "Still, despite my attempts to quell it, jealousy stirs in my gut."
    s "Well, do you like him?"
    show bedroomcg1c at cgcenter
    "Huimin makes a face and I relax."
    h "No way. He thinks he's so good-looking but he's really just average. I can't stand him, actually."
    s "Hahaha! I wish I could see his reaction if you say that to his face."
    show bedroomcg1d at cgcenter
    "Huimin grins lazily, nuzzling her face into the pillow."
    h "Maybe I should surprise him for graduation. Give that inflated ego a good kick."
    "We giggle some more. I feel dizzy with joy, gloriously relieved that we were on the same side. That Huimin doesn't like him, after all."
    h "I don’t really want to sleep yet, Syira. Should we play a game too?"
    s "What game?"
    "I blink, shuffling closer."
    h "Truth or dare."
    s "Sure."
    h "Okay, truth or dare?"
    s "Um… truth."
    h "Have you ever had a crush on someone?"
    show bedroomcg1e at cgcenter
    "{i}Oh.{/i} I hadn’t expected her to ask something like that — so cliched and embarrassing, yet drawn so confidently from her lips."  
    "I suppose she won’t know who, even if I answered honestly."
    s "…Yes."
    "Huimin smiles."
    h "Now you ask me."
    show bedroomcg1f at cgcenter
    s "Truth or dare?"
    h "Hmm… truth."
    "I am a petty, immature teenager. Her question had flustered me, so I wanted to turn the tables back on her."
    s "Have you ever kissed someone?"
    "There is the slightest hint of a blush on Huimin’s cheeks, but she answers without wavering."
    h "Yes. At one of the camps."
    "My breath stills. {w}I hate that I asked even though I knew the answer would feel like a truck running me over."
    "My stupid, sensitive heart {i}hurt{/i} and I want to cry and end the game."
    show bedroomcg1g at cgcenter
    h "Now, it’s your turn again. Truth or dare?"
    "I stare at her, blinking slowly. Suddenly, I’m tired of honesty. My heart already feels raw, bleeding on my sleeve from just a few questions."
    s "Dare, whatever."
    h "I dare you to kiss me."
    show bedroomcg1h at cgcenter
    "My eyes go wide."
    s "W-what?"
    h "You haven’t kissed anyone before, right?"
    s "I– no, I haven’t, but…"
    h "It’s really nothing much, Syira."
    "No. {i}No.{/i}{w} It really isn’t ‘nothing much’.{w} I feel like I am going to die.{w} Here I am, with an embarrassing crush on a girl who is going to kiss me but she thinks it’s ‘nothing much’."
    scene syiraroomdark2 with dissolve
    "Huimin inches closer. I close my eyes, nerves keeping me frozen in place."
    show bedroomcg2a at cgcenter
    with dissolve
    play sound "audio/clothing2.mp3"    
    "She presses her lips to mine. A small, chaste, barely there kiss."
    "I had forgotten how it felt, but I’m so immersed in this memory that it comes back to me. It’s almost cruel how vivid it is."
    show bedroomcg2b at cgcenter
    play sound "audio/hissing-soft.mp3"
    "In the corner of my vision, I see a shape behind the curtain. That’s when I knew that this memory returning like this is Her —{w} the spirit in the banana tree, the demon I made my wish to.{w} This is her cruel way of dangling what I want so badly before my eyes."
    scene black with dissolve
    "Because despite Huimin kissing me that night, it was nothing more than a meaningless act. Years later, after I grew to accept my sexuality and plucked up the courage to tell her how I felt—"
    "She rejected me."
    h "I could try to date you, but I just think that in the end, I'll probably end up with a guy. So I don't want to waste your time."
    "She won't even give me a chance. She didn't think we had an ending together."
    "I get it. I really do. But as much as I've resigned to it — having this memory dragged up from the depths and made afresh once more, I just want her all over again."
    $ persistent.unlock_bedroom = True
    jump after_dream

label after_dream:
    scene chaletroomdark with fade
    "I see the bedroom again — I’m back at the chalet."
    "My body still feels prickly with phantom sensations. My chest feels tight with emotions, the weight of it so heavy that I feel nauseated, ready to bend over and throw up on the floor."
    stop music fadeout 3.0

if love >= 2:
    jump ending_love
else:
    jump ending_envy

label ending_envy:
    scene huimincg3 with dissolve
    play music "audio/bleak-v3.wav"
    play sound "audio/crying-ringing.mp3"
    "Huimin is lying on the bed, her body turned away from me. Her shoulders are shaking as she presses her face into the pillow and cries."
    h "I’m sorry…David, I’m so sorry."
    s "Huimin."
    "I put my hand on her shoulder. Do I want to comfort her? Or do I just want her to stop saying his name?"
    h "I don’t know how it happened…"
    s "Stop, it’s already—"
    "It’s already over. He’s already dead. I wished for it and I don’t regret it, so stop dwelling on it and look at me."
    "Look at me, please."
    h "Come back, I still…"
    "I pull away, my stomach dropping like a stone in the ocean. This must be the cruelest joke of all. I’m sure David is laughing in his grave. All this, and I’m still not enough."
    "Deep in my gut, I feel a gnawing pain."
    "It’s familiar — something I’ve known for years."
    "It’s the feeling when I see his arm around her waist in their photos, when she addresses him and touches his cheek, when Huimin picks him over and over and over again."
    "{i}I want her to be mine. I want her to be mine.{/i}"
    "I had dreamt of a slow but sweet romance."
    "I had dreamt of Huimin, the fearless girl who didn’t care what anyone else thought, leading me into it. And me, the introverted girl who struggled to even express a single opinion of my own, gladly following along."
    "But nothing happened. And all I have is a pathetic, twisted wish."
    $ persistent.unlock_huimin = True
    stop music fadeout 5.0
    play sound "audio/haunted.mp3"
    "Slowly, I begin to hear a hissing in my head. It starts soft, like wind pushing past the curtains. Then it grows louder, raspy voices in harsh, unfamiliar tongues."
    "Her."
    "Her whisper is the curl of a finger, a taut thread tugging on my feet."

    scene chaletback with fade
    play music "audio/Ritual.mp3" fadein 1.0
    "I’m back outside, looking into the backyard where we buried him. A harsh breeze cuts through the forest, raising goosebumps across my skin."
    "I stare at the mound of earth — at the grave we had dug for him."
    "{i}He’s right there,{/i} my mind supplies. {i}The boy I wanted to become.{/i}"
    "My gut stings, painful with all that I want but am still missing."
    "For the first time, I have a name for it — {i}hunger.{/i}"

    show endingviolencecg1 at cgcenter
    with dissolve
    play sound "audio/digging.mp3"
    "I drop to my knees and start digging."
    "The thoughts in my head begin to cease, replaced by the repetitive scrape of earth against my hands."
    "Then, I hit flesh."

    play sound "audio/jumpscare.mp3"
    show endingviolencecg2 at cgcenter
    with hpunch
    "Here is — his boyish jaw, adam’s apple and broad shoulders rotted away.{w} And she still loves him. Even though he hurt her, even though he…"
    "{i}Take what you want.{/i}"
    "The voice is in a tongue I shouldn’t recognise, but I know what it says. After all, it’s been in my head for a while."
    "Demon or devil, it doesn’t matter. She’s the one who heard me all those years ago. She’s the only one who knows how bad I’ve wanted this."
    "{i}Wear his skin, and your wish can come true too.{/i}"
    "The hollow ache in my stomach is all-consuming, something that threatens to eat me up from the inside out."

    show endingviolencecg4 at cgcenter
    with dissolve
    play sound "audio/gore1.mp3"
    "I reach forward, sinking my hands into flesh."
    "It breaks easily under my fingers. Blood slicks over my fingers, smearing over my hands."
    "I think about how I am taking him apart.{w} I think about how I am breaking his boyish features, his easy charm and whatever Huimin loved down to its elements again.{w} And now, I can build myself anew with it."
    "I bring my hands up to my lips."
    play sound "audio/gore2.mp3"
    "He is bitter and sweet, something I hate and something she loved.{w} I chew.{w} Flesh breaks against my teeth, tearing and tearing apart.{w} Blood runs over my tongue, down my lips and my throat."
    "For the first time, the gnawing pit in my stomach has settled."
    "{i}She can love me now.{/i}"
    "I feel relieved, even though the rot in my mouth makes me want to heave."
    h "S-Syira?"

    scene endingviolencecgfull with fade
    window hide dissolve
    pause
    "My head whips around. I see Huimin by the door, a phone cradled carefully in her hands."
    "She looks terrified."
    h "What…what are you doing?"
    play sound "audio/siren.mp3"
    "I hear sirens in the distance, red and blue lights flashing in the night."
    s "I wanted you to be mine."
    s "But you won’t even look at me. Not even after I killed him."
    s "So I wanted to be him. It was the only way."
    h "No, no…god."
    s "It was all I ever wished for, all those years ago."
    "The sirens are closer now, but it’s okay. I have all I ever wanted now."
    "Her voice has gone quiet for a while, too."
    "I begin to wonder if maybe there was really no malevolent spirit or demon, just me.{w} Just me who ruined Huimin and her dream, me whose jealous heart set us all on a trajectory towards hell."
    "It’s a hell I’d gladly accept."

    $ quick_menu = False
    $ persistent.unlock_endenvy = True
    scene endenvy with fade
    with Pause(2)

    jump credits

label ending_love:
    scene huimincg1 with dissolve
    play music "audio/bleak-v4.wav"
    "Huimin is lying on the bed, motionless."
    s "Do you remember the ritual we did when we were younger?"
    s "You wanted us to make a wish together."
    s "…But I wished for something else.{w} Maybe that’s why it didn’t come true. Maybe that’s why we didn’t stay best friends like you’d hoped for."
    s "Because I don’t just want to be friends.{w} I want you."
    "And today I know I always will.{w} That I will run to Huimin’s side without a single seed of doubt, that I will lie and kill and bury for her."
    "Even if she said not to waste my time on her, I will chase the imprint of her kiss forever."
    "I will feed the pieces of my dream into her, force my pleas and promises pass her lips even if I know she will always, always, spit them back out. I know that and I've known that for years and still the dream does not die."
    $ persistent.unlock_huimin = True

    scene huimincg2
    "Huimin opens her eyes."
    play sound "audio/horror-ringing-short.mp3"
    "I see the shadow from the backyard, the window, the one who twists my gut in ways both nauseating and intoxicating."
    "I see the red thread I had tied myself to her. The way she followed me through the forest, through the dark and through the years of my turbulent life."
    "Of course, this is the only way it can happen for me."
    h "Show me."
    "She reaches up, cupping my face in her hand."
    h "Show me that you want me. I’m waiting."

    scene black with dissolve
    "I don’t care that it feels wrong. I’m long past that. So I let her drag me down and kiss her."

    scene chaletroomdark with dissolve
    show endinglovecg1 at cgcenter
    with dissolve
    play sound "audio/clothing2.mp3"
    "Her lips are sweet, but as she opens her mouth to invite me in, the taste on my tongue turns sour. Just like rotten flesh.{w} It should repulse me, but something about it feels intoxicating."
    "I move to straddle her, wanting to be closer.{w} I imagine our bodies as broken puzzle pieces, forced together by a wish, bruising where we meet."
    "If it hurts enough, maybe we can be moulded into the shape of each other."

    show endinglovecg2 at cgcenter
    with dissolve
    play sound "audio/clothing2.mp3"
    "I run my hands along her stomach."
    "She moans, a soft and haunting sound. It strips me naked, desire rising in my gut like bile."
    "I push my fingers under her blouse, unearthing more and more bruises.{w} Red, purple and blue. The sum of her wounds, mapped out beneath my hands."
    "She’s beautiful.{w} I don’t care if this ruins me."
    "I don’t care if the pressure crushes my organs or if my secrets are spilled from my lips and never returned. I don’t care if she takes me apart and never puts me back together."
    "I’ll gladly be swallowed by a tide of her making."

    show endinglovecg3 at cgcenter
    with dissolve
    h "Syira…"
    "She curls her arms around my neck, pulling herself close. Her lips press against my throat."
    play sound "audio/horror-ringing-short.mp3"
    h "Do you know the price of your wish?"
    "I know she’s speaking against my skin, but I hear her voice inside my head, deep and guttural like an inhuman growl.{w} Suddenly, her nails grow sharp against my skin, scraping against my pulse. My body goes cold."
    "I swallow.{w} She must taste my fear through my throat.{w} She must know that as much as I am afraid, I will not run."
    "I feel her lips pull tight into a smile, all teeth against the jugular of my neck."
    play sound "audio/bite.mp3"
    scene black with dissolve
    h "It’s you."

    scene endinglovecgfull with fade
    window hide dissolve
    pause
    "I close my eyes."
    "I hope my blood is warm against her lips.{w} I hope my heart is as black as it feels.{w} And I hope that when she is done with me — that she will drag me straight to hell."
    "It doesn’t matter if it’s a bad ending as long as it’s one I can share with her."
    $ persistent.unlock_endlove = True
    $ quick_menu = False
    scene endlove with fade
    with Pause(2)
    jump credits

    
label credits:

    scene black with fade 
    with Pause(1)
    show credits1 with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(0.5)
    show credits2 with dissolve
    with Pause(3)
    scene black with dissolve
    with Pause(0.5)
    show credits3 with dissolve
    with Pause(3)
    scene black with dissolve
    with Pause(1.5)   
    show credits4 with dissolve
    with Pause(1.5)
    scene black with dissolve
    with Pause(0.5) 
    show credits5 with dissolve
    with Pause(1.5)
    scene black with dissolve
    with Pause(0.5)
    show credits6 with dissolve
    with Pause(1.5)
    scene black with dissolve
    with Pause(0.5)
    show credits7 with dissolve
    with Pause(1.5)
    scene black with dissolve
    with Pause(0.5)
    show credits8 with dissolve
    with Pause(1.5)
    scene black with dissolve
    with Pause(0.5)
    return
