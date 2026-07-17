from app.reranker.cross_encoder_reranker import (
    CrossEncoderReranker
)


class RerankerFactory:
    _instance = None

    @staticmethod
    def get_reranker():

        if RerankerFactory._instance is None:

            RerankerFactory._instance = (
                CrossEncoderReranker()
            )

        return RerankerFactory._instance