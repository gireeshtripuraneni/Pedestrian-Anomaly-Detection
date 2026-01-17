import cv2
import os

def convert_frames_to_video(frame_folder, output_video, fps=10):
    images = sorted(
        [img for img in os.listdir(frame_folder) if img.endswith(".jpg")],
        key=lambda x: int(x.replace("frame", "").replace(".jpg", ""))
    )

    if not images:
        print(f"⚠ No frames found in {frame_folder}")
        return

    first_frame = cv2.imread(os.path.join(frame_folder, images[0]))
    height, width, _ = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for img in images:
        frame = cv2.imread(os.path.join(frame_folder, img))
        video.write(frame)

    video.release()
    print(f"✅ Video saved: {output_video}")


