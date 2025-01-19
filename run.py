import asyncio
import logging
import sys
from dotenv import load_dotenv

from app.bot import main

load_dotenv()

if __name__ == "__main__":

    main()