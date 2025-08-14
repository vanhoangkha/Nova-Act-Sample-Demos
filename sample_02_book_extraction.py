#!/usr/bin/env python3
"""
📚 Sample 02: Extract Book List with Pydantic
Demo structured information extraction from Wikipedia
"""

import os
from pydantic import BaseModel
from nova_act import NovaAct

class Book(BaseModel):
    title: str
    author: str

class BookList(BaseModel):
    books: list[Book]

def get_books(year: int) -> BookList | None:
    """
    Get NYT bestseller books by year
    Returns BookList or None if error occurs
    """
    try:
        with NovaAct(
            starting_page=f"https://en.wikipedia.org/wiki/List_of_The_New_York_Times_number-one_books_of_{year}#Fiction",
            headless=True
        ) as nova:
            print(f"📖 Extracting books from year {year}...")
            
            # Use schema for structured data extraction
            result = nova.act(
                "Return the books in the Fiction list",
                schema=BookList.model_json_schema()
            )
            
            if not result.matches_schema:
                print(f"❌ Data doesn't match schema for year {year}")
                return None
            
            # Parse JSON into Pydantic model
            book_list = BookList.model_validate(result.parsed_response)
            return book_list
            
    except Exception as e:
        print(f"❌ Error extracting year {year}: {e}")
        return None

def main():
    """Demo information extraction with Pydantic schema"""
    
    # Check API key
    api_key = os.getenv('NOVA_ACT_API_KEY')
    if not api_key:
        print("❌ Please set NOVA_ACT_API_KEY")
        return
    
    print("📚 Sample 02: Extract Book List")
    print("=" * 40)
    print("🏗️ Using Pydantic schema for structured data")
    
    # Test with one year
    year = 2023
    book_list = get_books(year)
    
    if book_list:
        print(f"\n✅ Found {len(book_list.books)} books from {year}:")
        for i, book in enumerate(book_list.books, 1):
            print(f"   {i}. {book.title} - {book.author}")
    else:
        print(f"❌ Could not get book list for year {year}")
    
    print("\n💡 This example demonstrates:")
    print("   • Using Pydantic BaseModel")
    print("   • Schema validation with matches_schema")
    print("   • Structured data extraction")

if __name__ == "__main__":
    main()
