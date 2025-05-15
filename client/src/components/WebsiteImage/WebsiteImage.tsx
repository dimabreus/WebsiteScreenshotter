import type { FC } from "react";

interface Props {
    imageData: string | null;
}

const WebsiteImage: FC<Props> = ({ imageData }) => {
    return (
        <div className="website-image w-full max-h-[75vh] aspect-video">
            {imageData ? (
                <img
                    src={`data:image/png;base64,${imageData}`}
                    alt="Website snapshot"
                    className="max-h-[75vh] aspect-video rounded-md shadow-md mx-auto"
                />
            ) : (
                <div className="max-h-[75vh] aspect-video mx-auto flex items-center justify-center mx-auto bg-neutral-950 text-gray-400">
                    Enter the URL and click the camera button
                </div>
            )}
        </div>
    );
};

export default WebsiteImage;
