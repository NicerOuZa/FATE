package com.osx.broker.message;

public class MessageWraper {

    MessageExt  message;

    public MessageExt getMessage() {
        return message;
    }

    public void setMessage(MessageExt message) {
        this.message = message;
    }

    public long getIndexFileOffset() {
        return indexFileOffset;
    }

    public void setIndexFileOffset(long indexFileOffset) {
        this.indexFileOffset = indexFileOffset;
    }

    long  indexFileOffset;

    public long getIndexFileTotal() {
        return indexFileTotal;
    }

    public void setIndexFileTotal(long indexFileTotal) {
        this.indexFileTotal = indexFileTotal;
    }

    long  indexFileTotal;
}