import './App.sass';

import { useState } from 'react';

import WebsiteImage from './components/WebsiteImage/WebsiteImage';
import WebsiteUrlInput from './components/WebsiteUrlInput/WebsiteUrlInput';

const App = () => {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [imageData, setImageData] = useState<string | null>(null);

  const handleSubmit = async (targetUrl: string) => {
    if (!url) return;
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8800/take_screenshot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ website: targetUrl }),
      });

      const { data } = await res.json();
      
      setImageData(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };
  return (
    <div id='app'>
      <div className="wrapper">
        <div className='website-url-input-wrapper'>
          <WebsiteUrlInput
            value={url}
            onChange={setUrl}
            onSubmit={handleSubmit}
            loading={loading}
          />
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
