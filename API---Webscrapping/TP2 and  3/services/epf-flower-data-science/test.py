from src.services.training import train_model

if __name__ == "__main__":
    try:
        model_path = train_model()
        print(f"Model trained and saved at: {model_path}")
    except Exception as e:
        print(f"Error during model training: {e}")
