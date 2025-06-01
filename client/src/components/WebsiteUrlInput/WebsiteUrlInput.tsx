import './WebsiteUrlInput.sass';

import { useState } from 'react';

import { PhotoCameraOutlined } from '@mui/icons-material';

import type { ChangeEvent, FC, KeyboardEvent } from "react";

interface Props {
    value: string;
    error: string | null;
    loading: boolean;
    onChange: (newUrl: string) => void;
    onSubmit: (fullUrl: string) => void;
}

const WebsiteUrlInput: FC<Props> = ({ value, error, loading, onChange, onSubmit }) => {
    const [protocol, setProtocol] = useState<"http://" | "https://">("https://");

    const handleKey = (e: KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") {
            onSubmit(protocol + value);
        }
    };

    return (
        <div className="website-url-input w-full max-w-2xl mx-auto mb-6">
            <div className="flex w-full items-center rounded-md overflow-hidden bg-neutral-900 text-white">
                <select
                    value={protocol}
                    onChange={(e) => setProtocol(e.target.value as ("http://" | "https://"))}
                    disabled={loading}
                    className="bg-neutral-900 px-3 py-3 text-gray-400 focus:outline-none"
                >
                    <option value="http://">http://</option>
                    <option value="https://">https://</option>
                </select>

                <input
                    type="text"
                    placeholder="example.com"
                    value={value}
                    onChange={(e: ChangeEvent<HTMLInputElement>) => onChange(e.target.value)}
                    onKeyDown={handleKey}
                    className="flex-grow bg-transparent px-4 py-3 text-white placeholder-gray-400 focus:outline-none"
                    disabled={loading}
                />

                <button
                    onClick={() => onSubmit(protocol + value)}
                    disabled={loading}
                    className="px-4 py-3 hover:bg-neutral-800 transition-colors flex items-center justify-center"
                >
                    {loading
                        ? <PhotoCameraOutlined className="camera-btn loading" />
                        : <PhotoCameraOutlined className="camera-btn" />
                    }
                </button>
            </div>

            <p className='text-red-400 leading-10'>{error}</p>
        </div>
    );
};

export default WebsiteUrlInput;