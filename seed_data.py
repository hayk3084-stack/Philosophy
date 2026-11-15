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
    {
        "title": "A Treatise of Human Nature",
        "kind": "book",
        "publish_year": 1739,
        "philosopher": "David Hume",
    },
    {
        "title": "An Enquiry Concerning Human Understanding",
        "kind": "book",
        "publish_year": 1748,
        "philosopher": "David Hume",
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
        "name": "Cogito argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "In the Second Meditation, after doubting the senses, the body and even mathematics, Descartes looks for one thing that cannot be doubted. Even if an all-powerful deceiver deceives him in everything, he must exist in order to be deceived: as long as he thinks he is something, he cannot be nothing. The proposition 'I am, I exist' is therefore necessarily true whenever he conceives it. He then asks what this 'I' is and answers that it is a thinking thing: a thing that doubts, understands, affirms, denies, wills and imagines. This first certainty becomes the foundation on which he rebuilds knowledge.",
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
    {
        "name": "Hume's copy principle",
        "writing": "A Treatise of Human Nature",
        "philosopher": "David Hume",
        "description": "Hume divides all perceptions of the mind into impressions, which are lively and forceful (sensations, passions, emotions), and ideas, which are their faint copies in thinking and reasoning. Every simple idea is derived from a simple impression that it exactly resembles, and the impression always comes first: a person born blind has no idea of colour. Complex ideas are built from simple ones, so the test of any philosophical term is to ask from what impression its idea is derived. Even the idea of God arises from reflecting on the operations of our own mind and augmenting its qualities of goodness and wisdom without limit.",
    },
    {
        "name": "Hume's fork",
        "writing": "An Enquiry Concerning Human Understanding",
        "philosopher": "David Hume",
        "description": "In Section IV of the Enquiry Hume divides all objects of human reason into two kinds. Relations of ideas, such as the truths of geometry and arithmetic, are discovered by thought alone and their denial implies a contradiction, but they say nothing about what exists. Matters of fact, such as that the sun will rise tomorrow, can be denied without contradiction and can only be known through experience. There is no third kind: no truth about what exists can be demonstrated by reason alone, and any claim that is neither a relation of ideas nor grounded in experience should be committed to the flames.",
    },
    {
        "name": "Hume's critique of causation",
        "writing": "A Treatise of Human Nature",
        "philosopher": "David Hume",
        "description": "Hume asks from what impression we derive the idea of a necessary connection between cause and effect. In any single case we observe only that one event is contiguous with and prior to another, never a power or necessity linking them. The connection cannot be known a priori either, since the denial of any causal claim implies no contradiction: anything may produce anything. After observing a constant conjunction of two kinds of events, the mind is carried by custom to expect one when it sees the other. The idea of necessary connection is copied from this internal feeling of expectation, not from anything in the objects. So causal inferences, and all reasoning from past to future, rest on habit rather than reason.",
    },
    {
        "name": "Hume's bundle theory of the self",
        "writing": "A Treatise of Human Nature",
        "philosopher": "David Hume",
        "description": "Some philosophers claim that we are intimately conscious of a self that is simple, identical and continuous over time. But if the idea of the self is real, it must come from some impression, and there is no constant impression of a self. When Hume enters most intimately into what he calls himself, he always stumbles on some particular perception, of heat or cold, light or shade, love or hatred, and never catches himself without a perception. The mind is therefore nothing but a bundle or collection of different perceptions that succeed one another with great rapidity, and the identity we ascribe to it is a fiction produced by the imagination.",
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
    {
        "source_arg": "Hume's copy principle",
        "relation_type": "based_on",
        "target_arg": "Locke's origin of ideas argument",
    },
    {
        "source_arg": "Hume's copy principle",
        "relation_type": "challenges",
        "target_arg": "Trademark argument",
    },
    {
        "source_arg": "Hume's critique of causation",
        "relation_type": "based_on",
        "target_arg": "Hume's copy principle",
    },
    {
        "source_arg": "Hume's critique of causation",
        "relation_type": "based_on",
        "target_arg": "Hume's fork",
    },
    {
        "source_arg": "Hume's critique of causation",
        "relation_type": "challenges",
        "target_arg": "Trademark argument",
    },
    {
        "source_arg": "Hume's bundle theory of the self",
        "relation_type": "based_on",
        "target_arg": "Hume's copy principle",
    },
    {
        "source_arg": "Hume's bundle theory of the self",
        "relation_type": "challenges",
        "target_arg": "Cogito argument",
    },
    {
        "source_arg": "Hume's bundle theory of the self",
        "relation_type": "challenges",
        "target_arg": "Real distinction argument",
    },
]
