import argparse
import whisper

def main():
    parser = argparse.ArgumentParser(
            description="Transcreve áudio em texto usando o Whisper."
            )
    parser.add_argument(
            '-m', '--model', type=str, required=True,
            help="O nome do modelo a ser usado (e.g. small, medium)."
            )
    parser.add_argument(
            '-f', '--file', type=str, required=True, 
            help="Caminho para o arquivo de áudio"
            )
    args = parser.parse_args()

    model = whisper.load_model(args.model)
    result = model.transcribe(args.file)
    print(result["text"])

if __name__ == "__main__":
    main()

