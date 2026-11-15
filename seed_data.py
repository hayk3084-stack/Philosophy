PHILOSOPHERS = [
    {
        "name": "René Descartes",
        "country": "France",
        "birth_year": 1596,
        "death_year": 1650,
        "school": "Rationalism",
        "catch_phrase": "I think therefore I am",
    },
    {
        "name": "David Hume",
        "country": "Scotland",
        "birth_year": 1711,
        "death_year": 1776,
        "school": "Empiricism",
        "catch_phrase": "Reason is, and ought only to be, the slave of the passions",
    },
    {
        "name": "Baruch Spinoza",
        "country": "Netherlands",
        "birth_year": 1632,
        "death_year": 1677,
        "school": "Rationalism",
        "catch_phrase": "God, or Nature",
    },
    {
        "name": "John Locke",
        "country": "England",
        "birth_year": 1632,
        "death_year": 1704,
        "school": "Empiricism",
        "catch_phrase": "No man's knowledge here can go beyond his experience",
    },
]

WRITINGS = [
    {
        "title": "Meditations",
        "kind": "book",
        "publish_year": 1641,
        "philosopher": "René Descartes",
    },
    {
        "title": "Ethics",
        "kind": "book",
        "publish_year": 1677,
        "philosopher": "Baruch Spinoza",
    },
    {
        "title": "An Essay Concerning Human Understanding",
        "kind": "book",
        "publish_year": 1690,
        "philosopher": "John Locke",
    },
]

ARGUMENTS = [
    {
        "name": "Senses argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "Descartes' first argument for doubt rests on the unreliability of the senses. Everything he had accepted as most true came to him through the senses, yet the senses have sometimes deceived him. Since it is unwise to fully trust anything that has deceived us even once, he concludes that beliefs based on the senses cannot be accepted as certain.",
    },
    {
        "name": "Dream argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "The dream argument pushes the doubt further. Even if the senses sometimes deceive us about distant or small things, it seems certain that I am sitting here by the fire, holding this paper. Yet he recalls that in dreams he has been just as convinced of such things while actually lying in bed. Since there are no certain signs by which waking can be distinguished from dreaming, he cannot be sure he is not dreaming right now, and so even his most immediate sensory experiences cannot be accepted as certain.",
    },
    {
        "name": "Error argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "In the Fourth Meditation Descartes explains how error is possible if God is no deceiver. Judgment involves two faculties: the intellect, which merely perceives ideas, and the will, which affirms or denies them. The intellect is finite, but the will is unlimited and free. Error arises when the will extends beyond what the intellect clearly and distinctly perceives and affirms what it does not fully understand. Error is therefore our own misuse of free will, not God's fault, and it can be avoided by suspending judgment until the perception is clear and distinct.",
    },
    {
        "name": "Real distinction argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "In the Sixth Meditation Descartes argues that the mind is really distinct from the body. Whatever he clearly and distinctly understands can be created by God separately. He has a clear and distinct idea of himself as a thinking, non-extended thing, and a clear and distinct idea of body as an extended, non-thinking thing. Therefore the mind and the body are two distinct substances, and the mind can exist without the body, even though in this life they are closely joined and interact with one another.",
    },
    {
        "name": "Trademark argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "In the Third Meditation Descartes finds in himself the idea of God, an infinite and perfect being. The cause of an idea must contain at least as much reality as the idea represents, and he, a finite and imperfect being, could not have produced the idea of the infinite himself. Nor could it come from the senses, since it never presented itself to him through them. Therefore the idea is innate: God placed it in him, like the mark a craftsman stamps on his work, and so God must exist.",
    },
    {
        "name": "Will and intellect argument",
        "writing": "Ethics",
        "philosopher": "Baruch Spinoza",
        "description": "In Part II (Propositions 48-49) Spinoza argues that there is no free will and that will and intellect are one and the same. The will is not a separate faculty that adds affirmation to an idea: every idea, by its very nature, already involves affirmation or denial. To have the idea of a triangle is already to affirm that its angles equal two right angles. Since the will is nothing beyond the particular affirmations involved in ideas, it cannot extend further than the intellect. Error is therefore not a misuse of free will but a privation of knowledge that comes from inadequate ideas, and what seems like suspending judgment is only the perception that our idea is inadequate.",
    },
    {
        "name": "Mind-body parallelism argument",
        "writing": "Ethics",
        "philosopher": "Baruch Spinoza",
        "description": "Spinoza argues that there is only one substance, God or Nature, and that thought and extension are two of its attributes, each conceived through itself. Because the attributes are conceptually independent, a mode of one attribute cannot cause a mode of another, so mind and body do not interact. Instead, the order and connection of ideas is the same as the order and connection of things (Part II, Proposition 7): the human mind is the idea of the human body, and mind and body are one and the same thing conceived under two different attributes. There are therefore no two distinct substances, only one reality expressed in two parallel ways.",
    },
    {
        "name": "Locke's argument against innate ideas",
        "writing": "An Essay Concerning Human Understanding",
        "philosopher": "John Locke",
        "description": "In Book I Locke attacks the doctrine that some ideas and principles are stamped on the mind from birth. The main support for the doctrine is universal assent, but there is no principle to which all people assent: children and those with severe intellectual disabilities have no thought of principles such as 'whatever is, is'. Even if universal assent existed, it could be explained in another way. And it is a contradiction to say that a truth is imprinted on the mind yet the mind does not perceive it. Saying that innate ideas are known once reason is used proves nothing, since by that standard every truth reason discovers would count as innate.",
    },
    {
        "name": "Locke's origin of ideas argument",
        "writing": "An Essay Concerning Human Understanding",
        "philosopher": "John Locke",
        "description": "In Book II Locke argues that the mind begins as white paper, void of all characters, and that all its ideas come from experience through two sources: sensation, which gives ideas of external things, and reflection, which gives ideas of the mind's own operations. Complex ideas are built by combining, comparing and abstracting simple ones. Even the idea of God is formed this way: we take ideas of existence, power, knowledge and duration, drawn from reflection, and enlarge them with the idea of infinity, which comes from our ability to repeat any quantity without end. No idea therefore needs to be innate.",
    },
    {
        "name": "Locke's primary and secondary qualities argument",
        "writing": "An Essay Concerning Human Understanding",
        "philosopher": "John Locke",
        "description": "In Book II, chapter 8, Locke distinguishes between qualities of bodies. Primary qualities, such as solidity, extension, figure, motion and number, are inseparable from a body however it is divided, and our ideas of them resemble the qualities in the body. Secondary qualities, such as colours, sounds, tastes and smells, are nothing in the bodies themselves but powers to produce sensations in us through their primary qualities. Our ideas of secondary qualities therefore do not resemble anything in the objects: the same water can feel hot to one hand and cold to the other, but it cannot be both at once.",
    },
]

CONNECTIONS = [
    {
        "source_arg": "Dream argument",
        "relation_type": "based_on",
        "target_arg": "Senses argument",
    },
    {
        "source_arg": "Will and intellect argument",
        "relation_type": "refutes",
        "target_arg": "Error argument",
    },
    {
        "source_arg": "Mind-body parallelism argument",
        "relation_type": "challenges",
        "target_arg": "Real distinction argument",
    },
    {
        "source_arg": "Locke's argument against innate ideas",
        "relation_type": "challenges",
        "target_arg": "Trademark argument",
    },
    {
        "source_arg": "Locke's origin of ideas argument",
        "relation_type": "based_on",
        "target_arg": "Locke's argument against innate ideas",
    },
    {
        "source_arg": "Locke's origin of ideas argument",
        "relation_type": "refutes",
        "target_arg": "Trademark argument",
    },
    {
        "source_arg": "Locke's primary and secondary qualities argument",
        "relation_type": "based_on",
        "target_arg": "Locke's origin of ideas argument",
    },
]
