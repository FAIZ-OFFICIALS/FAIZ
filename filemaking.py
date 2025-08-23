import os
import sys
import importlib.util

def main():
    try:
        # .so فائل کو load کریں
        so_file = "filemaking.cpython-312.so"
        
        if os.path.exists(so_file):
            spec = importlib.util.spec_from_file_location("filemaking_module", so_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # اگر آپ کی .so فائل میں main فنکشن ہے تو اسے کال کریں
            if hasattr(module, 'main'):
                module.main()
            else:
                print("Error: main function not found in .so file")
        else:
            print("Error: .so file not found")
            
    except Exception as e:
        print(f"Error loading .so file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
