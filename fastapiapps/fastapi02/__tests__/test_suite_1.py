from fastapi.testclient import TestClient
from requests import Response

from dummygen import Dummygen
from main import app, booksdb, no_id


class TestDummygen:
    # @formatter:off
    gen_db_books_without_params = [{'Author': 'Author1',  'CoverImage': 'cover0000000001.jpg',  'ISBN': '0000000000001',  'Title': 'Title1',  'YearOfPublish': 1801}, {'Author': 'Author2',  'CoverImage': 'cover0000000002.jpg',  'ISBN': '0000000000002',  'Title': 'Title2',  'YearOfPublish': 1802}, {'Author': 'Author3',  'CoverImage': 'cover0000000003.jpg',  'ISBN': '0000000000003',  'Title': 'Title3',  'YearOfPublish': 1803}, {'Author': 'Author4',  'CoverImage': 'cover0000000004.jpg',  'ISBN': '0000000000004',  'Title': 'Title4',  'YearOfPublish': 1804}, {'Author': 'Author5',  'CoverImage': 'cover0000000005.jpg',  'ISBN': '0000000000005',  'Title': 'Title5',  'YearOfPublish': 1805}, {'Author': 'Author6',  'CoverImage': 'cover0000000006.jpg',  'ISBN': '0000000000006',  'Title': 'Title6',  'YearOfPublish': 1806}, {'Author': 'Author7',  'CoverImage': 'cover0000000007.jpg',  'ISBN': '0000000000007',  'Title': 'Title7',  'YearOfPublish': 1807}, {'Author': 'Author8',  'CoverImage': 'cover0000000008.jpg',  'ISBN': '0000000000008',  'Title': 'Title8',  'YearOfPublish': 1808}, {'Author': 'Author9',  'CoverImage': 'cover0000000009.jpg',  'ISBN': '0000000000009',  'Title': 'Title9',  'YearOfPublish': 1809}, {'Author': 'Author10',  'CoverImage': 'cover0000000010.jpg',  'ISBN': '0000000000010',  'Title': 'Title10',  'YearOfPublish': 1810}]
    # @formatter:on

    def test_generate_without_params(self):
        assert Dummygen.generate_with_index() == {
            "ISBN": "0000000000001",
            "Title": "Title1",
            "Author": "Author1",
            "YearOfPublish": 1801,
            "CoverImage": "cover0000000001.jpg"
        }

    def test_generate_with_param_0(self):
        assert Dummygen.generate_with_index(-1) == {
            "ISBN": "0000000000001",
            "Title": "Title1",
            "Author": "Author1",
            "YearOfPublish": 1801,
            "CoverImage": "cover0000000001.jpg"
        }
        assert Dummygen.generate_with_index(0) == {
            "ISBN": "0000000000001",
            "Title": "Title1",
            "Author": "Author1",
            "YearOfPublish": 1801,
            "CoverImage": "cover0000000001.jpg"
        }

    def test_generate_with_param_5(self):
        assert Dummygen.generate_with_index(5) == {
            "ISBN": "0000000000005",
            "Title": "Title5",
            "Author": "Author5",
            "YearOfPublish": 1805,
            "CoverImage": "cover0000000005.jpg"
        }

    def test_generate_with_param_50(self):
        assert Dummygen.generate_with_index(50) == {
            "ISBN": "0000000000050",
            "Title": "Title50",
            "Author": "Author50",
            "YearOfPublish": 1850,
            "CoverImage": "cover0000000050.jpg"
        }

    def test_gen_db_books_without_params(self):
        assert Dummygen.gen_db_books() == self.gen_db_books_without_params

    def test_gen_db_books_with_param_0(self):
        assert Dummygen.gen_db_books(-1) == []
        assert Dummygen.gen_db_books(0) == []

    def test_gen_db_books_with_param_1(self):
        assert Dummygen.gen_db_books(1) == [{
            "ISBN": "0000000000001",
            "Title": "Title1",
            "Author": "Author1",
            "YearOfPublish": 1801,
            "CoverImage": "cover0000000001.jpg"
        }]

    def test_gen_db_books_with_param_100(self):
        assert len(Dummygen.gen_db_books(100)) == 100


class TestMain:
    # todo test db conn in every test method
    # todo DB cleanup after tests
    client = TestClient(app)

    def test_home(self):
        response: Response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == "HOMEPAGE FOR BOOKS API."

    def test_get_books(self):
        response: Response = self.client.get("/books")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_book_by_isbn_422(self):
        """Wrong value provided, but path exists"""
        response: Response = self.client.get("/book/422")
        assert response.status_code == 422

    def test_get_book_by_isbn_found(self):
        """Should always exist because of populating DB"""
        response: Response = self.client.get("/book/0000000000001")
        assert response.status_code == 200
        assert list(response.json().keys()) == ["ISBN", "Title", "Author", "YearOfPublish", "CoverImage"]

    def test_get_book_by_isbn_not_found(self):
        """Should never exist because of invalid ISBN"""
        isbn = "XYZXYZXYZXYZ1"
        response: Response = self.client.get(f"/book/{isbn}")
        assert response.status_code == 200
        assert response.json() == {"msg": f"No book with ISBN {isbn}"}

    def test_get_books_by_author_422(self):
        """Wrong or no value provided, but path exists"""
        response: Response = self.client.get("/book?author")
        assert response.status_code == 422
        response: Response = self.client.get(f"/book?author=")
        assert response.status_code == 422
        response: Response = self.client.get(f"/book?author=X")
        assert response.status_code == 422

    def test_get_books_by_author_found(self):
        """Should always exist because of populating DB"""
        author = "Author1"
        response: Response = self.client.get(f"/book?author={author}")
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["ISBN", "Title", "Author", "YearOfPublish", "CoverImage"]

    def test_get_books_by_author_not_found(self):
        """Should never exist because of invalid Author"""
        author = "XYZXYZXYZXYZ1"
        response: Response = self.client.get(f"/book?author={author}")
        assert response.status_code == 200
        assert response.json() == {"msg": f"No books for author {author}"}

    def test_create_book_ok(self):
        """payload is OK and DB returned inserted object"""
        isbn = "1000000000001"
        payload = {
            "ISBN": "1000000000001",
            "Title": "1Title1",
            "Author": "1Author1",
            "YearOfPublish": 2001,
            "CoverImage": "1cover0000000001.jpg"
        }
        response: Response = self.client.post("/book", json=payload)
        assert response.status_code == 201
        assert response.json() == {"msg": "Added", "book": payload}
        assert booksdb.find_one({"ISBN": isbn}, no_id) == payload

    def test_create_book_not_ok(self):
        payload = {}
        response: Response = self.client.post("/book", json=payload)
        assert response.status_code == 400
        assert response.json().get("error") == "Model cannot be empty"
        payload = {
            "ISBN": "100000000001",
            "Title": "T",
            "Author": "A",
            "YearOfPublish": 1
        }
        response: Response = self.client.post("/book", json=payload)
        assert response.status_code == 400
        assert response.json().get("error") == "Validation error"

    def test_update_book_by_isbn_ok(self):
        isbn_to_update = "1000000000001"
        isbn_after = "1000000000002"
        payload = {
            "ISBN": "1000000000002",
            "Title": "1Title2",
            "Author": "1Author2",
            "YearOfPublish": 2002,
            "CoverImage": "1cover0000000002.jpg"
        }
        response: Response = self.client.put(f"/book/{isbn_to_update}", json=payload)
        assert response.status_code == 200
        assert response.json() == {"msg": f"Book with ISBN {isbn_to_update} updated"} or response.json() == {
            "msg": "Nothing to update"}
        assert booksdb.find_one({"ISBN": isbn_after}, no_id) == payload

    def test_update_book_by_isbn_not_ok(self):
        isbn = "1000000000002"
        payload = {}
        response: Response = self.client.put(f"/book/{isbn}", json=payload)
        assert response.status_code == 400
        assert response.json().get("error") == "Update model cannot be empty"
        isbn = "1000000000002"
        payload = {
            "ISBN": "100000000001",
            "Title": "T",
            "Author": "A",
            "YearOfPublish": 1
        }
        response: Response = self.client.put(f"/book/{isbn}", json=payload)
        assert response.status_code == 400
        assert response.json().get("error") == "Validation error"

    def test_delete_book_by_isbn_ok(self):
        isbn = "XYZXYZXYZXYZ1"
        response: Response = self.client.delete(f"/book/{isbn}")
        assert response.status_code == 200
        assert response.json().get("msg") == "Nothing to delete"
        isbn = "1000000000002"
        response: Response = self.client.delete(f"/book/{isbn}")
        assert response.status_code == 200
        assert response.json().get("msg") == f"Book with ISBN {isbn} deleted"

    def test_delete_book_by_isbn_not_ok(self):
        isbn = "X"
        response: Response = self.client.delete(f"/book/{isbn}")
        assert response.status_code == 422
