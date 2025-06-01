import './App.sass';

import { useState } from 'react';
import { useTurnstile } from 'react-turnstile';

import { takeScreenshot } from './api';
import TurnstileWidget from './components/TurnstileWidget/TurnstileWidget';
import WebsiteImage from './components/WebsiteImage/WebsiteImage';
import WebsiteUrlInput from './components/WebsiteUrlInput/WebsiteUrlInput';

const App = () => {
  const [url, setUrl] = useState<string>("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [imageData, setImageData] = useState<string | null>(null);
  const [turnstileToken, setTurnstileToken] = useState<string | null>(null);

  const turnstile = useTurnstile();

  const handleTurnstileSuccess = (token: string) => {
    console.log('got token', token);
    setTurnstileToken(token);
  };

  const handleTurnstileError = () => {
    setTurnstileToken(null);
  };

  const handleSubmit = async (targetUrl: string) => {
    if (!url || !turnstileToken) return;

    // TODO: Add client-side url validation

    setLoading(true);

    const [data, error] = await takeScreenshot(targetUrl, turnstileToken);

    setImageData(data);
    setError(error);

    setTurnstileToken(null);
    turnstile.reset();

    setLoading(false);
  };
  return (
    <div id='app'>
      <div className="wrapper">
        <div className="input">
          <div className='website-url-input-wrapper'>
            <WebsiteUrlInput
              value={url}
              error={error}
              loading={loading}
              onChange={setUrl}
              onSubmit={handleSubmit}
            />
          </div>

          <div className="turnslite-widget-wrapper flex justify-center">
            <TurnstileWidget
              onSuccess={handleTurnstileSuccess}
              onError={handleTurnstileError}
            />
          </div>
        </div>


        <div className="website-image-wrapper flex justify-center">
          <WebsiteImage
            imageData={imageData}
          />
        </div>
      </div>
    </div>
  )
}

export default App
