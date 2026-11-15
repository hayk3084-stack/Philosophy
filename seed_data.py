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
]
