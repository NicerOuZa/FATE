/*
 * Copyright 2019 The FATE Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.webank.ai.fate.eggroll.storage.service.model;

import com.webank.ai.fate.core.io.KeyValueBytesStoreSupplier;
import com.webank.ai.fate.core.io.KeyValueStore;
import com.webank.ai.fate.core.io.StoreInfo;

public class LevelDbKeyValueBytesStoreSupplier implements KeyValueBytesStoreSupplier {


    public LevelDbKeyValueBytesStoreSupplier() {

    }

    @Override
    public KeyValueStore get(StoreInfo info) {
        return new LevelDBStore(info);
    }
}
