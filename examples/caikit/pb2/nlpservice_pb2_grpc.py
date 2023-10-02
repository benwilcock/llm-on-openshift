# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bidistreamingtokenclassificationtaskrequest_pb2 as bidistreamingtokenclassificationtaskrequest__pb2
import classificationresults_pb2 as classificationresults__pb2
import generatedtextresult_pb2 as generatedtextresult__pb2
import generatedtextstreamresult_pb2 as generatedtextstreamresult__pb2
import serverstreamingtextgenerationtaskrequest_pb2 as serverstreamingtextgenerationtaskrequest__pb2
import textclassificationtaskrequest_pb2 as textclassificationtaskrequest__pb2
import textgenerationtaskrequest_pb2 as textgenerationtaskrequest__pb2
import tokenclassificationresults_pb2 as tokenclassificationresults__pb2
import tokenclassificationstreamresult_pb2 as tokenclassificationstreamresult__pb2
import tokenclassificationtaskrequest_pb2 as tokenclassificationtaskrequest__pb2


class NlpServiceStub(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TextGenerationTaskPredict = channel.unary_unary(
                '/caikit.runtime.Nlp.NlpService/TextGenerationTaskPredict',
                request_serializer=textgenerationtaskrequest__pb2.TextGenerationTaskRequest.SerializeToString,
                response_deserializer=generatedtextresult__pb2.GeneratedTextResult.FromString,
                )
        self.ServerStreamingTextGenerationTaskPredict = channel.unary_stream(
                '/caikit.runtime.Nlp.NlpService/ServerStreamingTextGenerationTaskPredict',
                request_serializer=serverstreamingtextgenerationtaskrequest__pb2.ServerStreamingTextGenerationTaskRequest.SerializeToString,
                response_deserializer=generatedtextstreamresult__pb2.GeneratedTextStreamResult.FromString,
                )
        self.TokenClassificationTaskPredict = channel.unary_unary(
                '/caikit.runtime.Nlp.NlpService/TokenClassificationTaskPredict',
                request_serializer=tokenclassificationtaskrequest__pb2.TokenClassificationTaskRequest.SerializeToString,
                response_deserializer=tokenclassificationresults__pb2.TokenClassificationResults.FromString,
                )
        self.BidiStreamingTokenClassificationTaskPredict = channel.stream_stream(
                '/caikit.runtime.Nlp.NlpService/BidiStreamingTokenClassificationTaskPredict',
                request_serializer=bidistreamingtokenclassificationtaskrequest__pb2.BidiStreamingTokenClassificationTaskRequest.SerializeToString,
                response_deserializer=tokenclassificationstreamresult__pb2.TokenClassificationStreamResult.FromString,
                )
        self.TextClassificationTaskPredict = channel.unary_unary(
                '/caikit.runtime.Nlp.NlpService/TextClassificationTaskPredict',
                request_serializer=textclassificationtaskrequest__pb2.TextClassificationTaskRequest.SerializeToString,
                response_deserializer=classificationresults__pb2.ClassificationResults.FromString,
                )


class NlpServiceServicer(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    def TextGenerationTaskPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerStreamingTextGenerationTaskPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenClassificationTaskPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidiStreamingTokenClassificationTaskPredict(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TextClassificationTaskPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NlpServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TextGenerationTaskPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.TextGenerationTaskPredict,
                    request_deserializer=textgenerationtaskrequest__pb2.TextGenerationTaskRequest.FromString,
                    response_serializer=generatedtextresult__pb2.GeneratedTextResult.SerializeToString,
            ),
            'ServerStreamingTextGenerationTaskPredict': grpc.unary_stream_rpc_method_handler(
                    servicer.ServerStreamingTextGenerationTaskPredict,
                    request_deserializer=serverstreamingtextgenerationtaskrequest__pb2.ServerStreamingTextGenerationTaskRequest.FromString,
                    response_serializer=generatedtextstreamresult__pb2.GeneratedTextStreamResult.SerializeToString,
            ),
            'TokenClassificationTaskPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.TokenClassificationTaskPredict,
                    request_deserializer=tokenclassificationtaskrequest__pb2.TokenClassificationTaskRequest.FromString,
                    response_serializer=tokenclassificationresults__pb2.TokenClassificationResults.SerializeToString,
            ),
            'BidiStreamingTokenClassificationTaskPredict': grpc.stream_stream_rpc_method_handler(
                    servicer.BidiStreamingTokenClassificationTaskPredict,
                    request_deserializer=bidistreamingtokenclassificationtaskrequest__pb2.BidiStreamingTokenClassificationTaskRequest.FromString,
                    response_serializer=tokenclassificationstreamresult__pb2.TokenClassificationStreamResult.SerializeToString,
            ),
            'TextClassificationTaskPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.TextClassificationTaskPredict,
                    request_deserializer=textclassificationtaskrequest__pb2.TextClassificationTaskRequest.FromString,
                    response_serializer=classificationresults__pb2.ClassificationResults.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'caikit.runtime.Nlp.NlpService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NlpService(object):
    """-- SERVICES ----------------------------------------------------------------

    """

    @staticmethod
    def TextGenerationTaskPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/caikit.runtime.Nlp.NlpService/TextGenerationTaskPredict',
            textgenerationtaskrequest__pb2.TextGenerationTaskRequest.SerializeToString,
            generatedtextresult__pb2.GeneratedTextResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerStreamingTextGenerationTaskPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/caikit.runtime.Nlp.NlpService/ServerStreamingTextGenerationTaskPredict',
            serverstreamingtextgenerationtaskrequest__pb2.ServerStreamingTextGenerationTaskRequest.SerializeToString,
            generatedtextstreamresult__pb2.GeneratedTextStreamResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenClassificationTaskPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/caikit.runtime.Nlp.NlpService/TokenClassificationTaskPredict',
            tokenclassificationtaskrequest__pb2.TokenClassificationTaskRequest.SerializeToString,
            tokenclassificationresults__pb2.TokenClassificationResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidiStreamingTokenClassificationTaskPredict(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/caikit.runtime.Nlp.NlpService/BidiStreamingTokenClassificationTaskPredict',
            bidistreamingtokenclassificationtaskrequest__pb2.BidiStreamingTokenClassificationTaskRequest.SerializeToString,
            tokenclassificationstreamresult__pb2.TokenClassificationStreamResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TextClassificationTaskPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/caikit.runtime.Nlp.NlpService/TextClassificationTaskPredict',
            textclassificationtaskrequest__pb2.TextClassificationTaskRequest.SerializeToString,
            classificationresults__pb2.ClassificationResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)