import argparse
import whisper

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Transcribe audio files using Whisper.")

    # Add the arguments
    parser.add_argument('-m', '--model', type=str, required=True, help="The name of the Whisper model to use (e.g., 'small', 'medium', 'large').")
    parser.add_argument('-f', '--file', type=str, required=True, help="The path to the MP3 file to transcribe.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Load the model
    model = whisper.load_model(args.model)

    # Transcribe the audio file
    result = model.transcribe(args.file)
    print(result["text"])

if __name__ == "__main__":
    main()

