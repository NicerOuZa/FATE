package com.osx.broker.eggroll;

import com.google.common.collect.Lists;
import com.webank.eggroll.core.meta.Meta;


import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class ErJob extends  BaseProto<Meta.Job> {



    public  ErJob(String id,String name,List<ErStore> inputs,
                  List<ErStore> outputs,
                  List<ErFunctor>  functors,
                  Map<String,String> options){
        this.id = id;
        this.name = name;
        this.inputs = inputs;
        this.outputs = outputs;
        this.functors =  functors;
        this.options = options;
    }
    String id;
    String name;
    List<ErStore> inputs;
    List<ErStore> outputs;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ErStore> getInputs() {
        return inputs;
    }

    public void setInputs(List<ErStore> inputs) {
        this.inputs = inputs;
    }

    public List<ErStore> getOutputs() {
        return outputs;
    }

    public void setOutputs(List<ErStore> outputs) {
        this.outputs = outputs;
    }

    public List<ErFunctor> getFunctors() {
        return functors;
    }

    public void setFunctors(List<ErFunctor> functors) {
        this.functors = functors;
    }

    public Map<String, String> getOptions() {
        return options;
    }

    public void setOptions(Map<String, String> options) {
        this.options = options;
    }

    List<ErFunctor> functors;
    Map<String,String> options;

    @Override
    Meta.Job toProto() {

       return  Meta.Job.newBuilder().setId(id).setName(name)
                .addAllFunctors(this.functors.stream().map(ErFunctor::toProto).collect(Collectors.toList())).
        addAllInputs(inputs.stream().map(ErStore::toProto).collect(Collectors.toList())).putAllOptions(options).build();

    }

    public static ErJob  parseFromPb(Meta.Job  job){

        if(job ==null)
            return null;
        String id =job.getId();
        String name = job.getName();
        Map<String,String> options = job.getOptionsMap();
        List<Meta.Store>  inputMeta =   job.getInputsList();
        List<ErStore>  input = Lists.newArrayList();
        if(inputMeta!=null) {
            input =  inputMeta.stream().map(ErStore::parseFromPb).collect(Collectors.toList());
        }
        List<Meta.Store>  outputMeta =  job.getOutputsList();
        List<ErStore>  output = Lists.newArrayList();
        if(output!=null){
            output = outputMeta.stream().map(ErStore::parseFromPb).collect(Collectors.toList());
        }
        List<ErFunctor>  functors = Lists.newArrayList();
        List<Meta.Functor> functorMeta =    job.getFunctorsList();
        if(functorMeta!=null){
            functors = functorMeta.stream().map(ErFunctor::parseFromPb).collect(Collectors.toList());
        }

        ErJob  erJob = new ErJob( id, name,input,
                 output,
                 functors,
                 job.getOptionsMap());
        return  erJob;
    }
}




//case class ErJob(id: String,
//                 name: String = StringConstants.EMPTY,
//                 inputs: Array[ErStore],
//                 outputs: Array[ErStore] = Array(),
//        functors: Array[ErFunctor],
//        options: Map[String, String] = Map[String, String]())