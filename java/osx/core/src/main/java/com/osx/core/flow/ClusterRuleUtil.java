package com.osx.core.flow;

public final class ClusterRuleUtil {

    public static boolean validId(Long id) {
        return id != null && id > 0;
    }

    private ClusterRuleUtil() {}
}