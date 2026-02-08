import nltk
import ssl
import urllib.request
import logging
import os
from datetime import datetime

# Run this script in an environment where NLTK is to be installed, without opening the interactive NLTK downloader GUI.
# This script sets up the SSL context if necessary and downloads essential NLTK data packages
# This is useful for automated setups where user interaction is not possible.
# It downloads the following packages: punkt, stopwords, vader_lexicon, wordnet, and averaged_perceptron_tagger.
# You can add or remove packages from the list as needed.

def setup_logging():
    """Configure logging for the NLTK installation process."""
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Create log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'nltk_install_{timestamp}.log')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # Also log to console
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"NLTK installation logging initialized. Log file: {log_file}")
    return logger

def setup_ssl_context():
    """Configure SSL context for NLTK downloads if needed."""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Attempting to configure SSL context for NLTK downloads")
        # Try to create unverified HTTPS context for environments with SSL issues
        _create_unverified_https_context = ssl._create_unverified_context
        logger.debug("SSL _create_unverified_context found")
    except AttributeError as e:
        # If _create_unverified_context doesn't exist, use default context
        logger.warning(f"SSL _create_unverified_context not available: {e}")
        logger.info("Using default SSL context")
        return
    else:
        # Set the default HTTPS context to unverified for NLTK downloads
        ssl._create_default_https_context = _create_unverified_https_context
        logger.info("SSL context configured successfully - using unverified HTTPS context")

def check_package_exists(package_name):
    """Check if an NLTK package is already installed."""
    logger = logging.getLogger(__name__)
    
    try:
        nltk.data.find(f'tokenizers/{package_name}')
        logger.debug(f"Package '{package_name}' already exists in tokenizers")
        return True
    except LookupError:
        pass
    
    try:
        nltk.data.find(f'corpora/{package_name}')
        logger.debug(f"Package '{package_name}' already exists in corpora")
        return True
    except LookupError:
        pass
    
    try:
        nltk.data.find(f'taggers/{package_name}')
        logger.debug(f"Package '{package_name}' already exists in taggers")
        return True
    except LookupError:
        pass
    
    logger.debug(f"Package '{package_name}' not found in local NLTK data")
    return False

def download_nltk_data():
    """Download essential NLTK data packages."""
    logger = logging.getLogger(__name__)
    
    logger.info("Starting NLTK data download process")
    
    # Configure SSL if needed
    setup_ssl_context()
    
    # Download specific packages instead of opening the interactive installer
    packages = [
        'punkt',          # Tokenizer models
        'stopwords',      # Stop words corpus
        'vader_lexicon',  # Sentiment analysis
        'wordnet',        # WordNet lexical database
        'averaged_perceptron_tagger'  # POS tagger
    ]
    
    logger.info(f"Packages to download: {packages}")
    
    successful_downloads = []
    failed_downloads = []
    skipped_downloads = []
    
    for package in packages:
        logger.info(f"Processing package: {package}")
        
        # Check if package already exists
        if check_package_exists(package):
            logger.info(f"Package '{package}' already installed - skipping")
            print(f"⚠ {package} already installed")
            skipped_downloads.append(package)
            continue
        
        try:
            logger.info(f"Downloading package: {package}")
            result = nltk.download(package, quiet=True)
            
            if result:
                logger.info(f"Successfully downloaded package: {package}")
                print(f"✓ Downloaded {package}")
                successful_downloads.append(package)
            else:
                logger.error(f"Download returned False for package: {package}")
                print(f"✗ Failed to download {package}: Download returned False")
                failed_downloads.append(package)
                
        except ssl.SSLError as e:
            logger.error(f"SSL error downloading {package}: {e}")
            print(f"✗ SSL error downloading {package}: {e}")
            failed_downloads.append(package)
        except urllib.error.URLError as e:
            logger.error(f"URL error downloading {package}: {e}")
            print(f"✗ Network error downloading {package}: {e}")
            failed_downloads.append(package)
        except Exception as e:
            logger.error(f"Unexpected error downloading {package}: {e}", exc_info=True)
            print(f"✗ Failed to download {package}: {e}")
            failed_downloads.append(package)
    
    # Summary logging
    logger.info("NLTK download process completed")
    logger.info(f"Successful downloads: {successful_downloads}")
    logger.info(f"Failed downloads: {failed_downloads}")
    logger.info(f"Skipped downloads: {skipped_downloads}")
    
    # Print summary
    print("\n" + "="*50)
    print("NLTK Installation Summary:")
    print(f"✓ Successfully downloaded: {len(successful_downloads)} packages")
    print(f"✗ Failed downloads: {len(failed_downloads)} packages")
    print(f"⚠ Already installed: {len(skipped_downloads)} packages")
    
    if failed_downloads:
        logger.warning("Some packages failed to download. Check the logs for details.")
        print(f"\nFailed packages: {failed_downloads}")
        return False
    else:
        logger.info("All packages downloaded successfully!")
        print("\n🎉 All packages downloaded successfully!")
        return True

def verify_installation():
    """Verify that the downloaded packages work correctly."""
    logger = logging.getLogger(__name__)
    
    logger.info("Starting installation verification")
    
    verification_tests = [
        ('punkt', lambda: nltk.word_tokenize("Hello world!")),
        ('stopwords', lambda: set(nltk.corpus.stopwords.words('english'))),
        ('vader_lexicon', lambda: nltk.sentiment.vader.SentimentIntensityAnalyzer()),
        ('wordnet', lambda: nltk.corpus.wordnet.synsets('dog')),
        ('averaged_perceptron_tagger', lambda: nltk.pos_tag(['Hello', 'world']))
    ]
    
    for package_name, test_func in verification_tests:
        try:
            logger.info(f"Verifying package: {package_name}")
            result = test_func()
            logger.info(f"Package '{package_name}' verification successful")
            print(f"✓ {package_name} verification passed")
        except Exception as e:
            logger.error(f"Package '{package_name}' verification failed: {e}")
            print(f"✗ {package_name} verification failed: {e}")

if __name__ == "__main__":
    # Setup logging
    logger = setup_logging()
    
    try:
        logger.info("=== NLTK Installation Script Started ===")
        
        # Download NLTK data
        success = download_nltk_data()
        
        if success:
            # Verify installation
            verify_installation()
        
        logger.info("=== NLTK Installation Script Completed ===")
        
    except KeyboardInterrupt:
        logger.warning("Script interrupted by user")
        print("\n⚠ Script interrupted by user")
    except Exception as e:
        logger.critical(f"Unexpected error in main execution: {e}", exc_info=True)
        print(f"💥 Critical error: {e}")
        raise