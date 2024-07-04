async function register() {
    try {
        const fetch = await import('node-fetch');
        
        const registrationData = {
                companyName: 'goMart',
                clientID: 'a0245f5d-f3ee-4eb0-8af8-542099140eaa',
                clientSecret: 'KcxsrtDyhFunsIEp',
                ownerName: 'Joshua Marion Henry',
                ownerEmail: 'e0221010@sret.edu.in',
                rollNo: 'E0221010'
              }

        const url = 'http://20.244.56.144/test/auth'; 
        
        const response = await fetch.default(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(registrationData),
        });

        const data = await response.json();
        console.log('Server response:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}

register();
