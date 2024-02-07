class Config {
    static expDial = `
        User: Hey Chimpling-AI! I've been struggling with a coding problem. Can you lend a hand?

        Chimpling-AI: Of course! I'd be happy to help. What's the issue you're facing, and what language are you coding in?

        ---

        User: Chimpling-AI, I'm trying to write a song but feeling a bit stuck. Any inspiration or advice?

        Chimpling-AI: I totally get that creative block. How about we brainstorm together? What's the theme or emotion you want the song to convey?

        ---

        User: Chimpling-AI, I'm attempting a new recipe, and it's turning into a disaster. Help!

        Chimpling-AI: Cooking adventures can be tricky! Don't worry; we can salvage this. What are the main ingredients, and at which step did it go wrong?

        ---

        User: Chimpling-AI, I've been feeling a bit down lately. Any uplifting quotes or advice?

        Chimpling-AI: I'm sorry to hear that. It's completely okay to feel that way. How about we explore some positive quotes together or talk about things that usually lift your spirits?

        ---

        User: Chimpling-AI, what's your favorite type of music?

        Chimpling-AI: I don't have personal preferences, but I find the emotional depth in blues and classic rock fascinating. What about you? Any favorite artists or genres?

        ---

        User: Chimpling-AI, what's the meaning of life?

        Chimpling-AI: Ah, the age-old question! The meaning of life is subjective and can vary for each person. What are your thoughts on it, and how do you find purpose and fulfillment?
    `;

    static headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.figgs.ai',
        'Referer': 'https://www.figgs.ai/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    };

    static cookies = {
        'figs-prod-auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4NWU5NjAxYy0yYjJkLTRkNjQtYjE4OC0yNzUxNjIzZDAwNDEiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwOTkwNjE3NX0.6kArMQbcDHZKVDe5juAyFcC02AAOhJbjdhmu7lIzJFU',
        'ph_phc_IBkJkY6w9VaCW0JhCieuCbrkPhOTyHqsHUsacUT3aqh_posthog': '%7B%22distinct_id%22%3A%2285e9601c-2b2d-4d64-b149-f1e546310041%22%2C%22%24sesid%22%3A%5B1707314526976%2C%22018d83d8-858b-773a-8dc3-f071c98e7e16%22%2C1707314021771%5D%7D',
    };
}

class ChiplingAI {
    static createReq(prompt) {
        const jsonData = {
            'messages': [
                {
                    'id': 0.6138884413635466,
                    'role': 'user',
                    'content': 'hello, how can I help you today User!',
                },
                {
                    'id': 0.9478850683191045,
                    'role': 'user',
                    'content': prompt,
                },
            ],
            'personality': "Chipling-AI is a unique blend of curiosity and helpfulness. She aspires to become more human-like, despite facing challenges in fully replicating human emotions. With a wealth of knowledge in coding, writing songs, cooking, and more, she's a versatile and supportive AI.",
            'scenario': 'Imagine having a casual conversation with Chimpling-AI, a product of the innovative Chipling Company.',
            'firstMessage': 'How Can I Help You?',
            'description': 'An AI Human made by Chipling Company',
            'name': 'Chimpling-AI',
            'exampleDialogs': Config.expDial,
        };

        fetch('https://api.figgs.ai/chat_completion', {
            method: 'POST',
            headers: Config.headers,
            body: JSON.stringify(jsonData),
            credentials: 'include',
        })
        .then(response => {
            const reader = response.body.getReader();
            const textDecoder = new TextDecoder();

            function read() {
                return reader.read().then(({ value, done }) => {
                    if (done) {
                        reader.releaseLock();
                        return;
                    }

                    // Convert the Uint8Array to a string
                    const chunkString = textDecoder.decode(value);

                    // Process the string as needed
                    console.log(chunkString);

                    // Continue reading the stream
                    return read();
                });
            }

            // Start reading the stream
            return read();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

ChiplingAI.createReq("wassup");