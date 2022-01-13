import subprocess
import os
import json
import time
import edgeiq
from lift import CheckPosture


subprocess.check_call(['python','-m','pip','install','simpleaudio==1.0.4'])
import simpleaudio as sa

CONFIG_FILE = "config.json"
SCALE = "scale"

def load_json(filepath):
    if os.path.exists(filepath) == False:
        raise Exception('File at {} does not exist'.format(filepath))

    with open(filepath) as data:
        return json.load(data)

def main():
    config = load_json(CONFIG_FILE)
    scale = config.get(SCALE)

    pose_estimator = edgeiq.PoseEstimation("alwaysai/human-pose")

    pose_estimator.load(
            engine=edgeiq.Engine.DNN,
            accelerator=edgeiq.Accelerator.CPU)

    write_context = edgeiq.VideoWriter(output_path="vids/lifting.mp4")

    print("Loaded model:\n{}\n".format(pose_estimator.model_id))
    print("Engine: {}".format(pose_estimator.engine))
    print("Accelerator: {}\n".format(pose_estimator.accelerator))

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer, write_context as video_writer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()
            
            posture = CheckPosture(scale)

            # loop detection
            while True:
                frame = video_stream.read() # 480,640,3
                results = pose_estimator.estimate(frame)

                text = ["Model: {}".format(pose_estimator.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                for ind, pose in enumerate(results.poses):
                    if ind > 0:
                        continue
                    text.append("Person {}".format(ind))
                    text.append('-'*10)
                    text.append("Key Points:")

                    posture.set_key_points(pose.key_points)


                    correct_posture = posture.correct_posture()
                    if not correct_posture:
                        text.append(posture.build_message())
                        wave_obj = sa.WaveObject.from_wave_file("data/BendYourKnees.wav")
                        play_obj = wave_obj.play()
                        play_obj.wait_done()
                    if correct_posture:
                        # playsound("data/BendYourKnees.wav")
                        wave_obj = sa.WaveObject.from_wave_file("data/BendYourKnees.wav")
                        play_obj = wave_obj.play()
                        play_obj.wait_done()


                streamer.send_data(results.draw_poses(frame), text)
                video_writer.write_frame(frame)

                fps.update()

                if streamer.check_exit():
                    break
    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
