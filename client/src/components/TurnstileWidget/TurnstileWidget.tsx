import type { FC } from 'react';
import Turnstile from 'react-turnstile';

interface Props {
    onError?: (() => void) | undefined;
    onSuccess?: ((token: string) => void) | undefined;
}

const TurnstileWidget: FC<Props> = ({ onError, onSuccess }) => {
    const siteKey = import.meta.env.VITE_TURNSTILE_SITE_KEY;

    return (
        <div className='turnstile'>
            <Turnstile
                sitekey={siteKey}
                retry='auto'
                refreshExpired='auto'
                onError={onError}
                onVerify={onSuccess}
            />
        </div>
    )
}

export default TurnstileWidget