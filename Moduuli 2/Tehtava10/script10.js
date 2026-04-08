const numCandidates = parseInt(prompt("Number of candidates?"));
const candidates = [];

for (let i = 0; i < numCandidates; i++) {
    const name = prompt(`Name for candidate ${i + 1}`);
    candidates.push({
        name: name,
        votes: 0
    });
}

const numVoters = parseInt(prompt("Number of voters?"));

for (let i = 0; i < numVoters; i++) {
    let vote = prompt(`Voter ${i + 1}, who do you vote for?`);

    if (vote !== null && vote.trim() !== "") {
        vote = vote.trim();

        const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());

        if (candidate) {
            candidate.votes++;
        } else {
            console.log(`Vote for "${vote}" ignored: Candidate not found.`);
        }
    } else {
        console.log("Empty vote registered.");
    }
}

candidates.sort((a, b) => b.votes - a.votes);

if (candidates.length > 0) {
    console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
    console.log("results:");
    candidates.forEach(c => {
        console.log(`${c.name}: ${c.votes} votes`);
    });
} else {
    console.log("No candidates were entered.");
}