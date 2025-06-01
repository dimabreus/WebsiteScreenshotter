const apiUrl = import.meta.env.VITE_API_URL;

const ERRORS = {
    CONNECTION_REFUSED: "Unable to connect to the server.",
    UNPROCESSABLE_ENTITY: "Unknown error.",
    UNKNOWN_ERROR: "Unknown error.",
    INVALID_TURNSTILE: "Incorrect Captcha.",
    RATE_LIMITED: "Try again later.",
    INVALID_URL: "Invalid URL."
}

export const takeScreenshot = async (targetUrl: string, token: string): Promise<[result: string | null, error: string | null]> => {
    try {
        const res = await fetch(apiUrl + "take_screenshot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
                {
                    website: targetUrl,
                    turnstile_token: token
                }
            ),
        });

        const data = await res.json();

        if (res.status === 429) {
            return [null, ERRORS.RATE_LIMITED];
        }

        if (res.status === 422) {
            return [null, ERRORS.UNPROCESSABLE_ENTITY];
        }

        if (res.status === 400) {
            if (data.detail === "Turnstile verification failed") {
                return [null, ERRORS.INVALID_TURNSTILE];
            } else if (data.detail === "Invalid URL") {
                return [null, ERRORS.INVALID_URL];
            }
        }

        if (res.status === 200) {
            return [data.data, null];
        }

        console.warn("Unhandled API response", res.status, data);

        return [null, ERRORS.UNKNOWN_ERROR];

    } catch (error) {
        return [null, ERRORS.CONNECTION_REFUSED];
    }

}