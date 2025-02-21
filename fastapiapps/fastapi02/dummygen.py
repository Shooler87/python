class Dummygen:
    @staticmethod
    def generate_with_index(index: int = 1):
        if index <= 0: index = 1
        return {
            "ISBN": f"000{str(index):0>10}",
            "Title": "Title" + str(index),
            "Author": "Author" + str(index),
            "YearOfPublish": 1800 + index,
            "CoverImage": f"cover{str(index):0>10}.jpg"
        }

    @staticmethod
    def gen_db_books(count: int = 10):
        if count <= 0: return []
        return [Dummygen.generate_with_index(x) for x in range(1, count + 1)]